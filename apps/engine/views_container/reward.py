from apps.engine.views_container import (
    Reward,
    ListAPIView,
    permissions,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveAPIView,
    RewardSerializer,
    LimitOffsetPagination
)


class RewardListAPIView(ListAPIView):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = LimitOffsetPagination


class RewardDetailAPIView(RetrieveAPIView):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer
    permission_classes = [permissions.AllowAny]


class RewardCreateAPIView(CreateAPIView):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer
    permission_classes = [permissions.IsAuthenticated]


class RewardUpdateAPIView(UpdateAPIView):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer
    permission_classes = [permissions.IsAuthenticated]


class RewardDeleteAPIView(DestroyAPIView):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer
    permission_classes = [permissions.IsAuthenticated]