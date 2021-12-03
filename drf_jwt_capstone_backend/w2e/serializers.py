from rest_framework import serializers
from .models import RecipesToSave
from .models import Reviews
from .models import Reply
from .models import Rating


class RecipesToSaveSerializer (serializers.ModelSerializer):
    class Meta:
        model = RecipesToSave
        fields = ['user', 'recipe_id', 'title', 'image', 'image_type']

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ['recipe_id', 'review_id', 'comment_box', 'likes', 'dislikes']

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['review_id', 'reply_id', 'reply_box']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['review_id', 'rating_id', 'stars']