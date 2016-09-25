from rest_framework import viewsets
from .models import Cafe
from .serializers import CafeSerializer


class CafeViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = CafeSerializer
    queryset = Cafe.objects.all()
