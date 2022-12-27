from rest_framework import serializers
from . models import WinePal


class WinePalSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = WinePal
        fields = [
            'id', 'owner', 'created_on', 'updated_on', 'name',
            'bio', 'img', 'is_owner',
        ]
