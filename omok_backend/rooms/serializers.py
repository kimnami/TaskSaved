from rest_framework import serializers
from rooms.models import Room, History
from django.contrib.auth.models import User
from django.db.models import Sum
from django.db import models



class RoomSerializer(serializers.ModelSerializer):

    def get_turn(self, obj):
        try:
            recent = History.objects.filter(room_id = obj.id).order_by('id').reverse()[0]
        except IndexError:
            return 1

        if recent.player.id == obj.player1.id:
            return 2
        else:
            return 1

    def get_win(self, obj):
        return 0
        # history = History.objects.filter(room_id=obj.id)

    player1 = serializers.ReadOnlyField(source='player1.id')
    player2 = serializers.ReadOnlyField(source='player2.id')

    turn = serializers.SerializerMethodField(source='get_turn')
    win = serializers.SerializerMethodField(source='get_win')
    class Meta:
        model = Room
        fields = ('turn', 'win','player1','id','player2')

class HistorySerializer(serializers.ModelSerializer):

    player = serializers.ReadOnlyField(source='player.id')
    room = serializers.ReadOnlyField(source='room.id')

    class Meta:
        model = History
        fields = ('player', 'room','place_i','place_j')



class PlayerSerializer(serializers.BaseSerializer):
    def to_representation(self, obj):
        l1 = ([ obj.player1.id ] if obj.player1 else [])
        l2 = ([ obj.player2.id ] if obj.player2 else [])
        return l1 + l2

    class Meta:
        model = Room
