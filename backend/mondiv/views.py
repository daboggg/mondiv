from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated

from mondiv.models import Dividend
from mondiv.permissions import IsOwn
from mondiv.serializers import DividendSerializer


def test(request):
    return JsonResponse({'test': "tset"})


class DividendList(generics.ListCreateAPIView):
    serializer_class = DividendSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # print(self.request.query_params.get('start'),"AAAAAAAAAAAAA")
        params = self.request.query_params
        return Dividend.objects.filter(user=self.request.user,
                                       date_of_receipt__range=[params.get('start'), params.get('end')])
