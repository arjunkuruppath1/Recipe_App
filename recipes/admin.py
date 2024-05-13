from django.contrib import admin
from recipes.models import Recipe,Rating,Review

admin.site.register(Recipe)
admin.site.register(Rating)
admin.site.register(Review)
