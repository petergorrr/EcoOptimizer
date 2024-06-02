from rest_framework import serializers
from .models import EnergyData  # Assuming you have a model named EnergyData

class EnergyDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnergyData
        fields = '__all__'
