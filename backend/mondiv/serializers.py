from rest_framework import serializers

from mondiv.models import Dividend, Company, Currency, Account


############ Company ###################################
class CompanyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id','name', 'icon_image', 'ticker']


############ Currency ###################################
class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['id','name']


############ Account ###################################
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id','name']


############ Dividen ###################################
class DividendListSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # company = CompanySerializer()
    # company = serializers.PrimaryKeyRelatedField(read_only=True)
    # currency = CurrencySerializer()
    # account = AccountSerializer()

    class Meta:
        model = Dividend
        fields = '__all__'
        # fields = ['id','date_of_receipt', 'company', 'currency',
        #           'payoff', 'date_of_receipt', 'account','user']
        depth = 1


class DividendSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user = serializers.ReadOnlyField(source='author.username')

    def create(self, validated_data):
        return Dividend.objects.create(**validated_data)

    class Meta:
        model = Dividend
        fields = '__all__'