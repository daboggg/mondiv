from django.urls import path

from mondiv.views import *

urlpatterns = [
    path('test/', test),
    path('dividends/<int:pk>/', DividendDetail.as_view()),
    path('dividends/', DividendList.as_view()),
    path('currencies/', CurrencyList.as_view()),
    path('accounts/', AccountList.as_view()),
    path('companies_with_pagination/', CompanyListWithPagination.as_view()),
    path('companies/', CompanyList.as_view()),
    path('reports/', ReportList.as_view()),
    path('reports/<int:pk>/', ReportDetail.as_view()),
]
