from django.shortcuts import render
from rest_framework import viewsets
from api.models import PriceItem
from api.serializers import PriceItemSerializer


class PriceItemViewSet(viewsets.ModelViewSet):
    queryset = PriceItem.objects.all()
    serializer_class = PriceItemSerializer
