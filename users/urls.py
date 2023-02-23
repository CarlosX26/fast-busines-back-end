from django.urls import path
from users.views import UserView, UserViewById
from rest_framework_simplejwt import views

urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/<int:id>/", UserViewById.as_view()),
    path("users/login/", views.TokenObtainPairView.as_view()),
]
