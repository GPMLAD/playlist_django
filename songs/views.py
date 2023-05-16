from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from rest_framework.pagination import PageNumberPagination
from .serializers import SongSerializer
from albums.models import Album
from rest_framework import generics


class SongsResultsSetPagination(PageNumberPagination):
    page_size = 1


class SongView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Song.objects.all()
    serializer_class = SongSerializer
    pagination_class = SongsResultsSetPagination

    def perform_create(self, serializer) -> None:
        album_obj = Album.objects.get(pk=self.kwargs.get("pk"))
        serializer.save(album=album_obj)
