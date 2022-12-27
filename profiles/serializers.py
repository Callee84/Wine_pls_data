from rest_framework import serializers
from . models import WinePal


class WinePalSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = WinePal
        fields = [
            'id', 'owner', 'created_on', 'updated_on', 'name',
            'bio', 'img',
        ]
