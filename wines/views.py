from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from .models import Wine
from .serializers import WineSerializer
from wnpls_data.permissions import IsOwnerOrReadOnly


class WineList(generics.ListCreateAPIView):
    serializer_class = WineSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Wine.objects.all()
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        # DjangoFilterBackend
    ]
    search_fields = [
        'producer',
        'name',
    ]
    ordering_fields = [
        'name',
        'producer',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
