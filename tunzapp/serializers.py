from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import *


class FinancialNeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialNeed
        fields = '__all__'

class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donor
        fields = '__all__'

class ChildSerializer(serializers.ModelSerializer):
    needs = FinancialNeedSerializer(many=True)
    donors = DonorSerializer(many=True)
    class Meta:
        model = Child
        fields = '__all__'
