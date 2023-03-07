from rest_framework import serializers

from mondiv.models import Dividend, Company, Currency, Account


class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'icon_image', 'ticker']


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['name']


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['name']


class DividendSerializer(serializers.ModelSerializer):
    company = CompanySerializers()
    currency = CurrencySerializer()
    account = AccountSerializer()
    class Meta:
        model = Dividend
        fields = ['id','date_of_receipt', 'company', 'currency',
                  'payoff', 'date_of_receipt', 'account']