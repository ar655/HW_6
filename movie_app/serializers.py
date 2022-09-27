from rest_framework import serializers

from .models import *

class DirectorListSerializer(serializers.ModelSerializer):
    movies = serializers.SerializerMethodField()
    movies_count = serializers.SerializerMethodField()
    class Meta:
        model = Director
        fields = 'id name movies_count movies '.split()

    def get_movies_count(self,obj_director):
        return obj_director.movies.count()

    def get_movies(self,obj_director):
        return [director.title for director in obj_director.movies.all()]



class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text  movie'.split()


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title description duration director'.split()




class MoviesReviewsListSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = ' title rating reviews '.split()

    def get_reviews(self,obj_movie):
        return [review.text for review in obj_movie.reviews.all()]

    def get_rating(self, obj_movie):
        summ = 0
        for rate in obj_movies.reviews.all():
            summ + rate.stars
        return round(summ / obj_movies.reviews.count(),1) if obj_movie.count() else 'no rating'
