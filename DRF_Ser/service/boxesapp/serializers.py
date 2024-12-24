from rest_framework import serializers

from .models import Box, Item


class BoxSerializer(serializers.ModelSerializer):

    class Meta:
        model = Box
        fields = [
            'pk', 'name',
            'damaged',
            'height', 'width'
        ]


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = [
            'pk', 'name',
            'value',
            'box'
        ]
