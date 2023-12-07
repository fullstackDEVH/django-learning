from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import (
    AllUsersView,
    UserView,
    RegisterUserView,
    ActivitiesListAPIView,
    ActivitiesCreateAPIView,
    ActivitiesDeleteAPIView,
    ActivitiesDetailAPIView,
    ActivitiesUpdateAPIView,
    UserActivitiesAPIView
)

urlpatterns = [
    path("users", AllUsersView.as_view()),
    path("users/detail", UserView.as_view()),
    path("register/", RegisterUserView.as_view()),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),


    ## api for activities 
    path("activities/", ActivitiesListAPIView.as_view(), name="api-activities-list"),
    path('activities/<uuid:user_id>/user/', UserActivitiesAPIView.as_view(), name='api-user-activities'),
    path(
        "activities/<uuid:pk>/",
        ActivitiesDetailAPIView.as_view(),
        name="api-activities-detail",
    ),
    path(
        "activities/create/",
        ActivitiesCreateAPIView.as_view(),
        name="api-activities-create",
    ),
    path(
        "activities/<uuid:pk>/update/",
        ActivitiesUpdateAPIView.as_view(),
        name="api-activities-update",
    ),
    path(
        "activities/<uuid:pk>/delete/",
        ActivitiesDeleteAPIView.as_view(),
        name="api-activities-delete",
    ),
]
