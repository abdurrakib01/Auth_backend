from django.urls import path
from .views import UserRegistraionView, UserLoginView, UserProfileView,UserChagePasswordView,SendPasswordResetView
from .views import UserPasswordResetView
urlpatterns = [
    path('profile/', UserProfileView.as_view(), name="user"),
    path('register/', UserRegistraionView.as_view(), name='registration'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('changepassword/', UserChagePasswordView.as_view(), name='changepassword'),
    path('send-password-reset/', SendPasswordResetView.as_view(), name="send-password-reset"),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='resetview'),
]