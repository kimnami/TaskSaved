from debtpages_rest.models import Debt
from debtpages_rest.serializers import DebtSerializer, UserSerializer,UsersumSerializer
from rest_framework import generics
from django.contrib.auth.models import User




class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UsersumList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsersumSerializer



class UsersumDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UsersumSerializer


class DebtList(generics.ListCreateAPIView):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer


    def perform_create(self, serializer):
        serializer.save()


class DebtDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer
