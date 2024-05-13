from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from recipes.views import UserRegistrationView, UserLoginView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet, RatingViewSet, ReviewViewSet,RecipeSearchView


router = DefaultRouter()
router.register(r'recipes', RecipeViewSet)
router.register(r'ratings', RatingViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('api/register/', UserRegistrationView.as_view(), name='user-registration'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('recipes/search/', RecipeSearchView.as_view(), name='recipe-search'),

    path('', include(router.urls)),


]