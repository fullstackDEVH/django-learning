from apps.engine.views_container import (
    Staking,
    ListAPIView,
    permissions,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveAPIView,
    StakingSerializer,
    LimitOffsetPagination
)


class StakingListAPIView(ListAPIView):
    queryset = Staking.objects.all()
    serializer_class = StakingSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = LimitOffsetPagination


class StakingDetailAPIView(RetrieveAPIView):
    queryset = Staking.objects.all()
    serializer_class = StakingSerializer
    permission_classes = [permissions.IsAuthenticated]


class StakingCreateAPIView(CreateAPIView):
    queryset = Staking.objects.all()
    serializer_class = StakingSerializer
    permission_classes = [permissions.IsAuthenticated]

    # override the default method create
    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)
        return super().perform_create(serializer)


class StakingUpdateAPIView(UpdateAPIView):
    queryset = Staking.objects.all()
    serializer_class = StakingSerializer
    permission_classes = [permissions.IsAuthenticated]


class StakingDeleteAPIView(DestroyAPIView):
    queryset = Staking.objects.all()
    serializer_class = StakingSerializer
    permission_classes = [permissions.IsAuthenticated]