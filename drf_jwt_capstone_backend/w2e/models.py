from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class RecipesToSave(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    label = models.CharField(max_length=50, default="")

class Reviews(models.Model):
    recipe = models.CharField(max_length=50)
    comment_box =models.TextField(max_length=500)

class Rating (models.Model):
    review =models.ForeignKey(Reviews, on_delete=models.CASCADE)
    stars =models.IntegerField(default=0, null=False)

    def __str__(self):
        return self.title


