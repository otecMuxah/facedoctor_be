from rest_framework import serializers
from api.models import PriceItem, PriceSubGroup, PriceGroup


class PriceGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceGroup
        fields = ['id', 'name']


class PriceSubGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceSubGroup
        fields = ['id', 'name']


class PriceItemSerializer(serializers.ModelSerializer):
    group = PriceGroupSerializer(many=False)
    sub_group = PriceSubGroupSerializer(many=False)

    class Meta:
        model = PriceItem
        fields = ('id', 'name', 'description', 'price', 'group', 'sub_group')
