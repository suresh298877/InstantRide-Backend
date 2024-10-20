from django.urls import path
from . import views


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path("home/", views.home, name="home"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register, name="register"),


    # token authentication urls
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # api's

    # users
    path('api/register/', views.ApiCreateUser.as_view(), name="create_user")
]
