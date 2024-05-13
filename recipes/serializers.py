from django.contrib.auth.models import User
from rest_framework import serializers
from recipes.models import Recipe,Rating,Review


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email','password')

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        instance.is_active = True
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['recipe','rating']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['recipe','comment']