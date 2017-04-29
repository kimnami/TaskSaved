from accounts.models import Account
from django.contrib.auth.models import User
from accounts.serializers import AccountSerializer,UserSerializer
from rest_framework import generics




# class AccountList(generics.ListAPIView):

#     def get_queryset(self):
#         return Account.objects.get(user_username=self.username)
#     # queryset = Account.objects.all()
#     serializer_class = AccountSerializer


class AccountRegister(generics.CreateAPIView):
    serializer_class = AccountSerializer
    def perform_create(self, serializer):
        serializer.save()
