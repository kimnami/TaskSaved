from rooms.models import Room, History
from rooms.serializers import PlayerSerializer, HistorySerializer, RoomSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rooms.permissions import IsOmokAdmin
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status





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
    serializer_class = HistorySerializer
    # permission_classes = (IsUserOrReadOnly,)
    def get_queryset(self):
        return History.objects.filter(room_id=self.kwargs.get('pk'))

    def perform_create(self, serializer):
        try:
            pre_post_player = History.objects.filter(room_id=self.kwargs.get('pk')).order_by('-id')[0].player
        except IndexError:
            pre_post_player = -1

        if self.request.user != pre_post_player:
            if self.request.user == Room.objects.get(pk=self.kwargs.get('pk')).player1:
                serializer.save(player=self.request.user, room=Room.objects.get(pk=self.kwargs.get('pk')))
            elif self.request.user == Room.objects.get(pk=self.kwargs.get('pk')).player2:
                serializer.save(player=self.request.user, room=Room.objects.get(pk=self.kwargs.get('pk')))
            else:
                Response(status=status.HTTP_403_FORBIDDEN)





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
