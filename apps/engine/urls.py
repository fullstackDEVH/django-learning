from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views_container.token import MyTokenObtainPairView 
from rest_framework.authtoken import views 

from apps.engine.views import (
    AllUsersView,
    UserView,
    RegisterUserView,

    ActivitiesListAPIView,
    ActivitiesCreateAPIView,
    ActivitiesDeleteAPIView,
    ActivitiesDetailAPIView,
    ActivitiesUpdateAPIView,
    UserActivitiesAPIView,

    NotificationsListAPIView,
    NotificationsCreateAPIView,
    NotificationsDeleteAPIView,
    NotificationsDetailAPIView,
    NotificationsUpdateAPIView,

    StakingListAPIView,
    StakingCreateAPIView,
    StakingDeleteAPIView,
    StakingDetailAPIView,
    StakingUpdateAPIView,

    UserStakingListAPIView,
    UserStakingCreateAPIView,
    UserStakingDeleteAPIView,
    UserStakingDetailAPIView,
    UserStakingUpdateAPIView,

    TransactionListAPIView,
    TransactionCreateAPIView,
    TransactionDeleteAPIView,
    TransactionDetailAPIView,
    TransactionUpdateAPIView,

    FinancialTransactionsListAPIView,
    FinancialTransactionsCreateAPIView,
    FinancialTransactionsDeleteAPIView,
    FinancialTransactionsDetailAPIView,
    FinancialTransactionsUpdateAPIView,

    RewardListAPIView,
    RewardCreateAPIView,
    RewardDeleteAPIView,
    RewardDetailAPIView,
    RewardUpdateAPIView,

    SystemInformationListAPIView,
    SystemInformationCreateAPIView,
    SystemInformationDeleteAPIView,
    SystemInformationDetailAPIView,
    SystemInformationUpdateAPIView,
)

urlpatterns = [
    path("users", AllUsersView.as_view()),
    path("users/detail", UserView.as_view()),
    path("register", RegisterUserView.as_view()),
    path("token/auth", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify", TokenVerifyView.as_view(), name="token_verify"),

    path("activities/", ActivitiesListAPIView.as_view(), name="api-activities-list"),
    path('activities/<uuid:user_id>/user', UserActivitiesAPIView.as_view(), name='api-user-activities'),
    path(
        "activities/<uuid:pk>",
        ActivitiesDetailAPIView.as_view(),
        name="api-activities-detail",
    ),
    path(
        "activities/create",
        ActivitiesCreateAPIView.as_view(),
        name="api-activities-create",
    ),
    path(
        "activities/<uuid:pk>/update",
        ActivitiesUpdateAPIView.as_view(),
        name="api-activities-update",
    ),
    path(
        "activities/<uuid:pk>/delete",
        ActivitiesDeleteAPIView.as_view(),
        name="api-activities-delete",
    ),

    path("notifications", NotificationsListAPIView.as_view(), name="api-notifications-list"),
    path(
        "notifications/<uuid:pk>",
        NotificationsDetailAPIView.as_view(),
        name="api-notifications-detail",
    ),
    path(
        "notifications/create",
        NotificationsCreateAPIView.as_view(),
        name="api-notifications-create",
    ),
    path(
        "notifications/<uuid:pk>/update",
        NotificationsUpdateAPIView.as_view(),
        name="api-notifications-update",
    ),
    path(
        "notifications/<uuid:pk>/delete",
        NotificationsDeleteAPIView.as_view(),
        name="api-notifications-delete",
    ),

    
    path("staking", StakingListAPIView.as_view(), name="api-staking-list"),
    path(
        "staking/<uuid:pk>",
        StakingDetailAPIView.as_view(),
        name="api-staking-detail",
    ),
    path(
        "staking/create",
        StakingCreateAPIView.as_view(),
        name="api-staking-create",
    ),
    path(
        "staking/<uuid:pk>/update",
        StakingUpdateAPIView.as_view(),
        name="api-staking-update",
    ),
    path(
        "staking/<uuid:pk>/delete",
        StakingDeleteAPIView.as_view(),
        name="api-staking-delete",
    ),

    path("user-staking", UserStakingListAPIView.as_view(), name="api-user-staking-list"),
    path(
        "user-staking/<uuid:pk>",
        UserStakingDetailAPIView.as_view(),
        name="api-user-staking-detail",
    ),
    path(
        "user-staking/create",
        UserStakingCreateAPIView.as_view(),
        name="api-user-staking-create",
    ),
    path(
        "user-staking/<uuid:pk>/update",
        UserStakingUpdateAPIView.as_view(),
        name="api-user-staking-update",
    ),
    path(
        "user-staking/<uuid:pk>/delete",
        UserStakingDeleteAPIView.as_view(),
        name="api-user-staking-delete",
    ),

    path("transaction", TransactionListAPIView.as_view(), name="api-transaction-list"),
    path(
        "transaction/<uuid:pk>",
        TransactionDetailAPIView.as_view(),
        name="api-transaction-detail",
    ),
    path(
        "transaction/create",
        TransactionCreateAPIView.as_view(),
        name="api-transaction-create",
    ),
    path(
        "transaction/<uuid:pk>/update",
        TransactionUpdateAPIView.as_view(),
        name="api-transaction-update",
    ),
    path(
        "transaction/<uuid:pk>/delete",
        TransactionDeleteAPIView.as_view(),
        name="api-transaction-delete",
    ),


    path("financial-transaction", FinancialTransactionsListAPIView.as_view(), name="financial-transaction-list"),
    path(
        "financial-transaction/<uuid:pk>",
        FinancialTransactionsDetailAPIView.as_view(),
        name="api-financial-transaction-detail",
    ),
    path(
        "financial-transaction/create",
        FinancialTransactionsCreateAPIView.as_view(),
        name="api-financial-transaction-create",
    ),
    path(
        "financial-transaction/<uuid:pk>/update",
        FinancialTransactionsUpdateAPIView.as_view(),
        name="api-financial-transaction-update",
    ),
    path(
        "financial-transaction/<uuid:pk>/delete",
        FinancialTransactionsDeleteAPIView.as_view(),
        name="api-financial-transaction-delete",
    ),

    
    path("reward", RewardListAPIView.as_view(), name="api-reward-list"),
    path(
        "reward/<uuid:pk>",
        RewardDetailAPIView.as_view(),
        name="api-reward-detail",
    ),
    path(
        "reward/create",
        RewardCreateAPIView.as_view(),
        name="api-reward-create",
    ),
    path(
        "reward/<uuid:pk>/update",
        RewardUpdateAPIView.as_view(),
        name="api-reward-update",
    ),
    path(
        "reward/<uuid:pk>/delete",
        RewardDeleteAPIView.as_view(),
        name="api-reward-delete",
    ),


    path("system-information", SystemInformationListAPIView.as_view(), name="api-system-information-list"),
    path(
        "system-information/<uuid:pk>",
        SystemInformationDetailAPIView.as_view(),
        name="api-system-information-detail",
    ),
    path(
        "system-information/create",
        SystemInformationCreateAPIView.as_view(),
        name="api-system-information-create",
    ),
    path(
        "system-information/<uuid:pk>/update",
        SystemInformationUpdateAPIView.as_view(),
        name="api-system-information-update",
    ),
    path(
        "system-information/<uuid:pk>/delete",
        SystemInformationDeleteAPIView.as_view(),
        name="api-system-information-delete",
    ),
]
