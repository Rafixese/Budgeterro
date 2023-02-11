from django.contrib import admin
from .models import BudgetObj


# Register your models here.
@admin.register(BudgetObj)
class BudgetObjAdmin(admin.ModelAdmin):
    list_display = ('id', 'budget_name', 'created_by', 'created_at', 'updated_at')
