from rest_framework import serializers

from .models import BudgetObj


class BudgetObjSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetObj
        fields = ['id', 'budget_name', 'created_by', 'created_at', 'updated_at']
        read_only_fields = ('created_by', 'created_at', 'updated_at')
