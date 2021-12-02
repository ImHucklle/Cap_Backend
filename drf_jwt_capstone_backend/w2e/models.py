from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class RecipesToSave(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_id = models.IntegerField(default=0, null=False)
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=150)
    image_type= models.CharField(max_length=10)

class Reviews(models.Model):
    recipe_id = models.ForeignKey(RecipesToSave, on_delete=models.CASCADE)
    review_id = models.IntegerField(default=0, null=False)
    comment_box =models.TextField(max_length=500)
    likes =models.IntegerField(default=0, null=False)
    dislikes =models.IntegerField(default=0, null=False)

class Reply (models.Model):
    review_id =models.ForeignKey(Reviews, on_delete=models.CASCADE)
    reply_id =models.IntegerField(default=0, null=False)
    reply_box =models.TextField(max_length=500)

class Rating (models.Model):
    review_id =models.ForeignKey(Reviews, on_delete=models.CASCADE)
    rating_id =models.IntegerField(default=0, null=False)
    stars =models.IntegerField(default=0, null=False)

    def __str__(self):
        return self.title


