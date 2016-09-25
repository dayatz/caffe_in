from rest_framework import viewsets
from .models import Cafe, Menu, Gallery
from .serializers import CafeSerializer, GallerySerializer, MenuSerializer


class CafeViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = CafeSerializer
    queryset = Cafe.objects.all()


class MenuViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = MenuSerializer

    def get_queryset(self):
        return Menu.objects.filter(cafe_pk=self.kwargs.get('cafe_pk'))


class GalleryViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = GallerySerializer

    def get_query(self):
        return Gallery.objects.filter(cafe_pk=self.kwargs.get('cafe_pk'))
