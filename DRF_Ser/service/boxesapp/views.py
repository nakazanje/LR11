from rest_framework import viewsets

from .models import Box, Item
from .serializers import BoxSerializer, ItemSerializer


class BoxViewSet(viewsets.ModelViewSet):
    """
    View set for Box provides 'list', 'create', 'retriveve',
    'update' and 'destroy' actions.
    """
    queryset = Box.objects.all()
    serializer_class = BoxSerializer


class ItemViewSet(viewsets.ModelViewSet):
    """
    View set for Item provides 'list', 'create', 'retriveve',
    'update' and 'destroy' actions.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
