from rest_framework import serializers
from .models import RecipesToSave, Reviews, Reply, Rating


class RecipesToSaveSerializer (serializers.ModelSerializer):
    class Meta:
        model = RecipesToSave
        fields = ['user', 'recipe', 'title', 'image', 'image_type']

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ['recipe', 'comment_box', 'likes', 'dislikes']

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['review', 'reply_box']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['review', 'stars']