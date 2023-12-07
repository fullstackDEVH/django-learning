from apps.engine.views_container import (
    UserStaking,
    ListAPIView,
    permissions,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveAPIView,
    UserStakingSerializer,
    LimitOffsetPagination
)


class UserStakingListAPIView(ListAPIView):
    queryset = UserStaking.objects.all()
    serializer_class = UserStakingSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = LimitOffsetPagination


class UserStakingDetailAPIView(RetrieveAPIView):
    queryset = UserStaking.objects.all()
    serializer_class = UserStakingSerializer
    permission_classes = [permissions.AllowAny]


class UserStakingCreateAPIView(CreateAPIView):
    queryset = UserStaking.objects.all()
    serializer_class = UserStakingSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserStakingUpdateAPIView(UpdateAPIView):
    queryset = UserStaking.objects.all()
    serializer_class = UserStakingSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserStakingDeleteAPIView(DestroyAPIView):
    queryset = UserStaking.objects.all()
    serializer_class = UserStakingSerializer
    permission_classes = [permissions.IsAuthenticated]