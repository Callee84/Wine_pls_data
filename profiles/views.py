from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import WinePal
from .serializers import WinePalSerializer


class WinePalsList(APIView):
    def get(self, request):
        winepals = WinePal.objects.all()
        serializer = WinePalSerializer(winepals, many=True)
        return Response(serializer.data)


class WinePalDetails(APIView):
    serializer_class = WinePalSerializer

    def get_object(self, pk):
        try:
            winepal = WinePal.objects.get(pk=pk)
            return winepal
        except WinePal.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        winepal = self.get_object(pk)
        serializer = WinePalSerializer(winepal)
        return Response(serializer.data)

    def put(self, request, pk):
        winepal = self.get_object(pk)
        serializer = WinePalSerializer(winepal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)
