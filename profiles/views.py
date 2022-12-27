from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import WinePal
from .serializers import WinePalSerializer
from wnpls_data.permissions import IsOwnerOrReadOnly


class WinePalsList(generics.ListAPIView):
    queryset = WinePal.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
        ).order_by('-created_on')
    serializer_class = WinePalSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__following__followed__winepal',
        'owner__followed__owner__winepal',
    ]
    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'owner__followed__created_on',
        'owner__following__created_on'
    ]


class WinePalDetails(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile if you're the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = WinePal.objects.all()
    serializer_class = WinePalSerializer
    queryset = WinePal.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
        ).order_by('-created_on')
