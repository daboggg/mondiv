import json
from django.http import JsonResponse
from django.db.models import Q
from django.shortcuts import render
from rest_framework import generics, permissions, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from mondiv.models import Dividend, Currency, Account, Company, Report
from mondiv.permissions import IsOwner
from mondiv.serializers import DividendListSerializer, CurrencySerializer, AccountSerializer, DividendSerializer, \
    CompanyListSerializer, ReportListSerializer
from mondiv.utils import client


def test(request):
    return JsonResponse({'test': "tset"})


######### Dividend ###############################
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
        return Dividend.objects.filter(
            Q(company__name__icontains=params.get('search')) | Q(company__ticker__icontains=params.get('search')) | Q(
                account__name__icontains=params.get('search')),
            user=self.request.user,
            date_of_receipt__range=[params.get('start'), params.get('end')],

        ).order_by('id')

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
# class CompanyList(mixins.ListModelMixin, generics.GenericAPIView):
#     queryset = Company.objects.all()
#     serializer_class = CompanyListSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)


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


######### Company ###############################
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
            report_date__range=[params.get('start'), params.get('end')],
        ).order_by('id')
