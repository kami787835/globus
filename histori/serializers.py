from rest_framework import serializers
from .models import Stories, StoryVideos, Cards

class StoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stories
        fields = '__all__'

class StoryVideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryVideos
        fields = '__all__'

class CardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cards
        fields = '__all__'