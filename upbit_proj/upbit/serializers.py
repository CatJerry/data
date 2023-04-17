from rest_framework.serializers import ModelSerializer
from .models import CoinData,CoinName

class TestDataSerializer(ModelSerializer):
    class Meta:
        model = CoinName
        fields = '__all__'