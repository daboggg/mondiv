import json
import os
import datetime
import calendar
from datetime import timedelta

import requests
from django.contrib.auth.decorators import login_required
from django.db.models.functions import TruncYear, TruncMonth
from django.http import JsonResponse
from django.db.models import Q, Sum
from django.shortcuts import render
from rest_framework import generics, permissions, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_409_CONFLICT
from rest_framework.views import APIView

from mondiv.models import Dividend, Currency, Account, Company, Report
from mondiv.permissions import IsOwner
from mondiv.serializers import DividendListSerializer, CurrencySerializer, AccountSerializer, DividendSerializer, \
    CompanyListSerializer, ReportListSerializer, ReportSerializer
from mondiv.utils import client, get_rus_month, rus_months


def test(request):
    return JsonResponse({'test': "tset"})


######### Dividend ###############################
class DividendListForChart(APIView):

    def get(self, request, format=None):
        params = request.query_params
        field_value_pairs = [
            ('user', self.request.user),
            ('date_of_receipt__range',
             [params.get('date_start', '2010-01-01'), params.get('date_end', datetime.date.today())]),
            # ('company__ticker', params.get('ticker')),
            ('currency__name', params.get('currency'))
        ]
        filter_options = {k: v for k, v in field_value_pairs if v}
        res = Dividend.objects.filter(**filter_options)

        # total_for_each_year
        if params.get('type') == 'total_for_each_year':
            res = res.annotate(year=(TruncYear('date_of_receipt'))) \
                .values('year') \
                .annotate(total=Sum('payoff')) \
                .order_by('year')
            return JsonResponse({'res': {
                'years': [r['year'].year for r in res],
                'total': [r['total'] for r in res],
            }})

        # last_year
        elif params.get('type') == 'last_year':
            res = res.annotate(year=TruncYear('date_of_receipt'),
                               month=TruncMonth('date_of_receipt')) \
                .values('year', 'month') \
                .annotate(total=Sum('payoff')) \
                .order_by('year')
            return JsonResponse({'res': {
                'month': [get_rus_month(r['month'].month) for r in res],
                'total': [r['total'] for r in res],
            }})

        # last_n_years
        elif params.get('type') == 'last_n_years':
            res = res.annotate(year=TruncYear('date_of_receipt'),
                               month=TruncMonth('date_of_receipt')) \
                .values('year', 'month') \
                .annotate(total=Sum('payoff')) \
                .order_by('year')

            result = {'month': rus_months, 'years': {}}

            for r in res:
                result['years'][r['year'].year] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

            for r in res:
                result['years'][r['year'].year][r['month'].month - 1] = r['total']

            return JsonResponse(result)

        # total_for_each_ticker
        elif params.get('type') == 'total_for_each_ticker':
            res = res.values('company__name').annotate(total=Sum('payoff'))

            return JsonResponse({
                'companyName': [r['company__name'] for r in res],
                'total': [r['total'] for r in res]
            })

        # total_for_each_account
        elif params.get('type') == 'total_for_each_account':
            res = res.values('account__name').annotate(total=Sum('payoff'))

            return JsonResponse({
                'accountName': [r['account__name'] for r in res],
                'total': [r['total'] for r in res]
            })

        # statistics
        elif params.get('type') == 'statistics':
            res = res.values('company__name', 'payoff').order_by('payoff')
            min_payment = res.first()
            max_payment = res.last()
            total = res.aggregate(total=Sum('payoff'))['total']
            total_payments = res.count()

            return JsonResponse({
                'minPayment': min_payment,
                'maxPayment': max_payment,
                'totalPayments': total_payments,
                'total': round(total, 2)
            })


class TotalPayoff(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        return JsonResponse(
            Dividend.objects.filter(user=self.request.user,
                                    company__ticker=self.request.query_params.get('ticker')
                                    ).aggregate(totalPayoff=Sum('payoff'))
        )


def dividendHistory(request):
    ticker = request.GET.get('ticker')
    limit = request.GET.get('limit', 40)
    apiKey = os.environ.get("POLYGON_API_KEY") or 'slfhowwfy'

    url = f'https://api.polygon.io/v3/reference/dividends?ticker={ticker}&limit={limit}&apiKey={apiKey}'
    res = requests.get(url)

    if len(res.json()['results']) != 0:
        res = res.json()['results']
        res = [[r['cash_amount'] for r in reversed(res)], [r['pay_date'] for r in reversed(res)]]
    else:
        url = f'http://iss.moex.com/iss/securities/{ticker}/dividends.json'
        res = requests.get(url)
        res = res.json()['dividends']['data']
        res = [[r[3] for r in res], [r[2] for r in res]]

    return JsonResponse({'res': res})


class DividendListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


class DividendList(generics.ListCreateAPIView):
    serializer_class = DividendListSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = DividendListPagination

    def get_queryset(self):
        params = self.request.query_params
        # return Dividend.objects.filter(
        #     Q(company__name__icontains=params.get('search')) | Q(company__ticker__icontains=params.get('search')) | Q(
        #         account__name__icontains=params.get('search')),
        #     user=self.request.user,
        #     date_of_receipt__range=[params.get('date_start'), params.get('date_end')],
        # ).order_by('id')
        field_value_pairs = [
            ('user', self.request.user),
            ('date_of_receipt__range',
             [params.get('date_start', '2010-01-01'), params.get('date_end', datetime.date.today())]),
            ('company__ticker', params.get('ticker'))
        ]
        filter_options = {k: v for k, v in field_value_pairs if v}
        return Dividend.objects.filter(
            Q(company__name__icontains=params.get('search', '')) | Q(
                company__ticker__icontains=params.get('search', '')) | Q(
                account__name__icontains=params.get('search', '')),
            **filter_options
        )

    def post(self, request, *args, **kwargs):
        serializer = DividendSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)

        return Response({'post': serializer.data})


class DividendDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dividend.objects.all()
    serializer_class = DividendSerializer
    permission_classes = [IsAuthenticated, IsOwner]


######### Currency ###############################
class CurrencyList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


######### Account ###############################
class AccountList(mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class = AccountSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Account.objects.filter(user=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


######### Company ###############################
class CompanyListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyListSerializer

    def post(self, request, *args, **kwargs):
        ticker = request.data['ticker'].upper()
        if Company.objects.filter(ticker=ticker).exists():
            return Response({'info': {'message': "Компания с таким тикером уже добавлена"}})
        else:
            try:
                res = client.get_ticker_details(ticker)
                company = Company()
                company.name = res.name
                company.ticker = res.ticker
                company.description = res.description
                company.icon_url = res.branding.icon_url
                company.get_remote_image()
                return Response({'info': {'message': "Компания добалена"}})
            except Exception as e:
                return Response({'info': json.loads(e.args[0])})


class CompanyListWithPagination(generics.ListCreateAPIView):
    serializer_class = CompanyListSerializer
    pagination_class = CompanyListPagination

    def get_queryset(self):
        params = self.request.query_params
        return Company.objects.filter(
            Q(name__icontains=params.get('search'))
            | Q(ticker__icontains=params.get('search'))
        ).order_by('id')


class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyListSerializer


######### Report ###############################
class ReportListForChart(APIView):

    def get(self, request, format=None):
        params = request.query_params
        field_value_pairs = [
            ('user', self.request.user),
            ('report_date__range',
             [params.get('date_start', '2010-01-01'), params.get('date_end', datetime.date.today())]),
            # ('company__ticker', params.get('ticker')),
            ('currency__name', params.get('currency'))
        ]
        filter_options = {k: v for k, v in field_value_pairs if v}
        reports = Report.objects.filter(**filter_options)

        # reports_for_each_company
        if params.get('type') == 'reports_for_each_company':

            result = {'data': {}}

            start = datetime.datetime.strptime('2022-12-01', '%Y-%m-%d').date()
            end = datetime.date.today()
            labels = []

            while start < end:
                labels.append(f'{get_rus_month(start.month)}-{start.year}')
                days_in_month = calendar.monthrange(start.year, start.month)[1]
                start += timedelta(days=days_in_month)
            result['labels'] = labels

            for account in Account.objects.filter(user=self.request.user):
                reportsByAccount = reports.filter(account=account) \
                    .order_by('report_date') \
                    .values('amount') \
                    .annotate(year=TruncYear('report_date'), month=TruncMonth('report_date'))

                data = {
                    f'{get_rus_month(r["month"].month)}-{r["year"].year}': r['amount']
                    for r in reportsByAccount
                }

                result['data'][account.name] = data
            return JsonResponse(result)

        # general_report
        elif params.get('type') == 'general_report':

            result = {'data': {}}

            start = datetime.datetime.strptime('2022-12-01', '%Y-%m-%d').date()
            end = datetime.date.today()
            labels = []

            while start < end:
                labels.append(f'{get_rus_month(start.month)}-{start.year}')
                days_in_month = calendar.monthrange(start.year, start.month)[1]
                start += timedelta(days=days_in_month)
            result['labels'] = labels

            res = reports.annotate() \
                .annotate(month=TruncMonth('report_date')) \
                .order_by('month')\
                .values('month') \
                .annotate(total=Sum('amount'))

            res = {f'{get_rus_month(r["month"].month)}-{r["month"].year}': r['total'] for r in res}
            result['data'] = res
            return JsonResponse(result)


class ReportListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


class ReportList(generics.ListCreateAPIView):
    serializer_class = ReportListSerializer
    pagination_class = ReportListPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        params = self.request.query_params
        return Report.objects.filter(
            user=self.request.user,
            report_date__range=[params.get('date_start'), params.get('date_end')],
        ).order_by('id')

    def post(self, request, *args, **kwargs):
        data = request.data
        if Report.objects.filter(user=self.request.user,
                                 report_date=data['report_date'],
                                 currency=data['currency'],
                                 account=data['account']).exists():
            return Response({'message': 'Этот отчет уже существует'}, status=HTTP_409_CONFLICT)

        else:
            serializer = ReportSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=self.request.user)

            return Response({'report': serializer.data})


class ReportDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated, IsOwner]
