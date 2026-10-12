from rest_framework import serializers
from .models import *

class ReviewSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'rating', 'text']


class ProductSerialayzer(serializers.ModelSerializer):
    reviews = ReviewSerialaizer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'category', 'owner', 'reviews']

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError('Sena doljna bit bolwe 0!')
        return value



