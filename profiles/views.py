from rest_framework.views import APIView
from rest_framework.response import Response
from .models import WinePal
from .serializers import WinePalSerializer


class WinePalsList(APIView):
    def get(self, request):
        winepals = WinePal.objects.all()
        serializer = WinePalSerializer(winepals, many=True)
        return Response(serializer.data)
