from debtpages_rest.models import Debt
from debtpages_rest.serializers import DebtSerializer, UserSerializer,UsersumSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from debtpages_rest.permissions import IslenderOrBorrowerReadOnly, IsRequestUser, IsDebtAdmin




class DebtList(generics.ListCreateAPIView):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer
    permission_classes = (IsDebtAdmin, )
    def perform_create(self, serializer):
        serializer.save(borrower=self.request.user)


class DebtDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer
    permission_classes = (
        IslenderOrBorrowerReadOnly, )

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsDebtAdmin, )


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsRequestUser,)

class UsersumList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsersumSerializer
    permission_classes = (IsDebtAdmin, )


class UsersumDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UsersumSerializer
    permission_classes = (IsRequestUser,)

