from rest_framework import serializers

from webapp.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class Serializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

