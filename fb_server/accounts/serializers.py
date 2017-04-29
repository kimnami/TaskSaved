from rest_framework import serializers
from django.contrib.auth.models import User
from accounts.models import Account
from django.db import models


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','username', 'last_name','first_name','password')


class AccountSerializer(serializers.ModelSerializer):

    #UserSerializer를 상속받음
    user = UserSerializer()

    class Meta:
        model = Account
        fields = ('user','gender','birthday')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        user.set_password(user_data['password'])
        user.save()
        account = Account.objects.create(user=user, **validated_data)
        return account
