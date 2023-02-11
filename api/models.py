from django.contrib.auth.models import User
from django.db import models


class BudgetObj(models.Model):
    budget_name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='BudgetObjects')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        permissions = [('can_manage_budgetobj', 'Can manage budget objects')]
        unique_together = ['budget_name', 'created_by']
