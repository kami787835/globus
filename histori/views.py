from rest_framework import generics
from .models import Stories, StoryVideos, Cards
from .serializers import StoriesSerializer, StoryVideosSerializer, CardsSerializer

class StoriesListCreateView(generics.ListAPIView):
    queryset = Stories.objects.all()
    serializer_class = StoriesSerializer

class StoryVideosListCreateView(generics.ListAPIView):
    queryset = StoryVideos.objects.all()
    serializer_class = StoryVideosSerializer


class CardsListCreateView(generics.ListAPIView):
    queryset = Cards.objects.all()
    serializer_class = CardsSerializer

class CardsDetailView(generics.RetrieveAPIView):
    queryset = Cards.objects.all()
    serializer_class = CardsSerializer