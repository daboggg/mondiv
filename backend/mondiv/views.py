from django.http import JsonResponse
from django.db.models import Q
from django.shortcuts import render
from rest_framework import generics, permissions, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from mondiv.models import Dividend, Currency, Account, Company
from mondiv.permissions import IsOwner
from mondiv.serializers import DividendListSerializer, CurrencySerializer, AccountSerializer, DividendSerializer, \
    CompanyListSerializer


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
            Q(company__name__icontains=params.get('search')) | Q(company__ticker__icontains=params.get('search')) | Q(account__name__icontains=params.get('search')),
            user=self.request.user,
            date_of_receipt__range=[params.get('start'), params.get('end')],

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
class CompanyList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyListSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
