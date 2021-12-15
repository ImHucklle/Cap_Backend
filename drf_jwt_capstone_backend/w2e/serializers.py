from rest_framework import serializers
from .models import RecipesToSave, Reviews, Reply, Rating


class RecipesToSaveSerializer (serializers.ModelSerializer):
    class Meta:
        model = RecipesToSave
        fields = ['user', 'label']

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ['recipe', 'comment_box']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['review', 'stars']