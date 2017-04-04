from rest_framework import serializers
from debtpages_rest.models import Debt
from django.contrib.auth.models import User
from django.db.models import Sum
from django.db import models



class DebtSerializer(serializers.ModelSerializer):
    borrower = serializers.ReadOnlyField(source='borrower.id')


    class Meta:
        model = Debt
        fields = ('id', 'created','amount','borrower','lender')

class UserSerializer(serializers.ModelSerializer):
    # debts_as_borrower = serializers.PrimaryKeyRelatedField(many=True, queryset=Debt.objects.all())
    # debts_as_lender = serializers.PrimaryKeyRelatedField(many=True, queryset=Debt.objects.all())


    class Meta:
        model = User
        fields = ('id','username','debts_as_borrower','debts_as_lender')

class UsersumSerializer(serializers.ModelSerializer):

    def get_lended_money(self, obj):
        total = 0
        q = Debt.objects.filter(lender_id = obj.id)
        for debt in q:
            total+= debt.amount
        return total

    def get_borrowed_money(self, obj):
        total = 0
        q = Debt.objects.filter(borrower_id = obj.id)
        for debt in q:
            total+= debt.amount
        return total

    borrowed_money = serializers.SerializerMethodField(source='get_borrowed_money')
    lended_money = serializers.SerializerMethodField(source='get_lended_money')


    class Meta:
        model = User
        fields = ('id', 'username','borrowed_money','lended_money')