from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import ObjCanDeleteBudgetObj

from .models import BudgetObj
from .serializers import BudgetObjSerializer


class BudgetObjViewSet(viewsets.ModelViewSet):
    queryset = BudgetObj.objects.all()
    serializer_class = BudgetObjSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticated]
        elif self.action == 'destroy':
            permission_classes = [IsAuthenticated, ObjCanDeleteBudgetObj]
        else:
            permission_classes = [IsAuthenticated, IsAdminUser]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        budget_obj = super().create(request, *args, **kwargs)
        assign_perm('view_budgetobj', request.user, budget_obj.data.serializer.instance)
        assign_perm('change_budgetobj', request.user, budget_obj.data.serializer.instance)
        assign_perm('delete_budgetobj', request.user, budget_obj.data.serializer.instance)
        return budget_obj

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
