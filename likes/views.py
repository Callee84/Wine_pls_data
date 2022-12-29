from rest_framework import generics, permissions
from wnpls_data.permissions import IsOwnerOrReadOnly
from likes.models import Likes, LikesWine
from likes.serializers import LikesSerializers, LikesWineSerializers


class LikesList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikesSerializers
    queryset = Likes.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikesListDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikesSerializers
    queryset = Likes.objects.all()


class LikesWineList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikesWineSerializers
    queryset = LikesWine.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikesWineListDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikesWineSerializers
    queryset = LikesWine.objects.all()
