from django.urls import path

from mondiv.views import test

urlpatterns = [
    path('test/', test),
]
