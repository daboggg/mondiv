from django.http import JsonResponse
from django.db.models import Q
from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from mondiv.models import Dividend
from mondiv.permissions import IsOwn
from mondiv.serializers import DividendSerializer


def test(request):
    return JsonResponse({'test': "tset"})


class DividendListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


class DividendList(generics.ListCreateAPIView):
    serializer_class = DividendSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = DividendListPagination

    def get_queryset(self):
        params = self.request.query_params
        return Dividend.objects.filter(
            Q(company__name__icontains=params.get('search')) | Q(company__ticker__icontains=params.get('search')) | Q(account__name__icontains=params.get('search')),
            user=self.request.user,
            date_of_receipt__range=[params.get('start'), params.get('end')],

        )
