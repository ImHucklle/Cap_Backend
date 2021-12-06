from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class RecipesToSave(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    recipe = models.IntegerField(default=0, null=False)
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=150)
    image_type= models.CharField(max_length=10)

class Reviews(models.Model):
    recipe = models.ForeignKey(RecipesToSave, on_delete=models.CASCADE)
    comment_box =models.TextField(max_length=500)
    likes =models.IntegerField(default=0, null=False)
    dislikes =models.IntegerField(default=0, null=False)

class Reply (models.Model):
    review =models.ForeignKey(Reviews, on_delete=models.CASCADE)
    reply_box =models.TextField(max_length=500)

class Rating (models.Model):
    review =models.ForeignKey(Reviews, on_delete=models.CASCADE)
    stars =models.IntegerField(default=0, null=False)

    def __str__(self):
        return self.title


