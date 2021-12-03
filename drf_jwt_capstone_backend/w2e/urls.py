from django.urls import path
from . import views

urlpatterns = [
    path('recipes/', views.RecipesToSaveList.as_view()),
    path('reviews/', views.ReviewsList.as_view()),
    path('reply/', views.ReplyList.as_view()),
    path('rating/', views.RatingList.as_view()), 
    path('recipes/<int:pk>/', views.RecipesToSaveDetail.as_view()),
    path('reviews/<int:pk>/', views.ReviewsDetail.as_view()),
    path('reply/<int:pk>/', views.ReplyDetail.as_view()),
    path('rating/<int:pk>/', views.RatingDetail.as_view())
]