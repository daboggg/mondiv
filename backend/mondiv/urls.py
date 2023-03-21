from django.urls import path

from mondiv.views import *

urlpatterns = [
    path('test/', test),
    path('dividends/', DividendList.as_view()),
    path('dividends/<int:pk>/', DividendDetail.as_view()),
]
