from rest_framework.serializers import ModelSerializer
from banking.models import BankingMethod


class MobileRechargeSerializer(ModelSerializer):
    class Meta:
        filmodel = BankingMethod
        fields = "__all__"
