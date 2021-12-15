from django.shortcuts import render
from django.http.response import Http404
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import RecipesToSaveSerializer, ReviewsSerializer, ReplySerializer, RatingSerializer
from .models import RecipesToSave, Reviews, Reply, Rating

# Create your views here.

class RecipesToSaveList(APIView):
    
    permissions_classes = [IsAuthenticated]
    def get(self, request):
        recipes = RecipesToSave.objects.all()
        serializer = RecipesToSaveSerializer(recipes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RecipesToSaveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RecipesToSaveDetail(APIView):

    permissions_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return RecipesToSave.objects.get(pk=pk)
        except RecipesToSave.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        recipes = self.get_object(pk)
        serializer = RecipesToSaveSerializer(recipes)
        return Response(serializer.data)

    def put(self, request, pk):
        recipes = self.get_object(pk)
        serializer = RecipesToSaveSerializer(recipes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        recipes = self.get_object(pk)
        recipes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ReviewsList(APIView):

    permissions_classes = [IsAuthenticated]
    def get(self, request):
        reviews = Reply.objects.all()
        serializer = ReviewsSerializer(reviews, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReviewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReviewsDetail(APIView):

    permissions_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Reviews.objects.get(pk=pk)
        except Reply.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        reviews = self.get_object(pk)
        serializer = ReviewsSerializer(reviews)
        return Response(serializer.data)

    def put(self, request, pk):
        reviews = self.get_object(pk)
        serializer = ReviewsSerializer(reviews, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        reviews = self.get_object(pk)
        reviews.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RatingList(APIView):

    permissions_classes = [IsAuthenticated]
    def get(self, request):
        ratings = Rating.objects.all()
        serializer = RatingSerializer(ratings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RatingDetail(APIView):

    permissions_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Rating.objects.get(pk=pk)
        except Rating.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        ratings = self.get_object(pk)
        serializer = RatingSerializer(ratings)
        return Response(serializer.data)

    def put(self, request, pk):
        ratings = self.get_object(pk)
        serializer = RatingSerializer(ratings, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        ratings = self.get_object(pk)
        ratings.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)