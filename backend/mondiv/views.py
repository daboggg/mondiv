from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics, permissions

from mondiv.models import Dividend
from mondiv.serializers import DividendSerializer


def test(request):
    return JsonResponse({'test': "tset"})


class DividendList(generics.ListCreateAPIView):
    queryset = Dividend.objects.all()
    serializer_class = DividendSerializer
    # permission_classes = [permissions.IsAuthenticated]
