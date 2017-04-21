from rooms.models import Room, History
from rooms.serializers import PlayerSerializer, HistorySerializer, RoomSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rooms.permissions import IsOmokAdmin, IsUserOrReadOnly
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response




class RoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (IsOmokAdmin, )
    def perform_create(self, serializer):
        serializer.save()


class RoomDetail(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

# class PlayerList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = PlayerSerializer
#     def perform_create(self, serializer):
#         serializer.save()


class HistoryList(generics.ListCreateAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
    permission_classes = (IsUserOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(player=self.request.user, room=Room.objects.get(pk=self.kwargs.get('pk')))





@api_view(['GET', 'POST'])
def room_players_list(request, pk):
    try:
        room = Room.objects.get(pk = pk)
    except Room.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    serializer = PlayerSerializer(room)
    if request.method == 'GET':
        return Response(serializer.data)
    elif request.method == 'POST':
        if room.player1 == None:
            room.player1 = request.user
            room.save()
        elif room.player2 == None:
            room.player2 = request.user
            room.save()
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
        return Response(status=status.HTTP_201_CREATED)
