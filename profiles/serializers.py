from rest_framework import serializers
from .models import WinePal
from followers.models import Follower


class WinePalSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            return following.id if following else None
        return None

    class Meta:
        model = WinePal
        fields = [
            'id', 'owner', 'created_on', 'updated_on', 'name',
            'bio', 'profile_image', 'is_owner', 'following_id',
            'posts_count', 'followers_count', 'following_count'
        ]
