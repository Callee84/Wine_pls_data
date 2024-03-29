from rest_framework import serializers
from .models import Comment, CommentWine


class CommentsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_on', 'updated_on',
            'post', 'comment',
        ]


class CommentDetailSerializer(CommentsSerializer):
    post = serializers.ReadOnlyField(source='post.id')


class CommentWineSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = CommentWine
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_on', 'updated_on',
            'wine', 'comment_wine',
        ]


class CommentWineDetailSerializer(CommentWineSerializer):
    wine = serializers.ReadOnlyField(source='wine.id')
