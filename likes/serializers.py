from django.db import IntegrityError
from rest_framework import serializers
from .models import Likes, LikesWine


class LikesSerializers(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Likes
        fields = [
            'id', 'owner', 'post'
            ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'Detail': 'I think you liked this post already'
            })


class LikesWineSerializers(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = LikesWine
        fields = [
            'id', 'owner', 'wine'
            ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'Detail': 'I think you liked this wine already'
            })

