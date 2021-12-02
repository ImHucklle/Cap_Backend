from django.contrib import admin
from .models import RecipesToSave
from .models import Reviews
from .models import Reply
from .models import Rating

# Register your models here.

admin.site.register(RecipesToSave)
admin.site.register(Reviews)
admin.site.register(Reply)
admin.site.register(Rating)