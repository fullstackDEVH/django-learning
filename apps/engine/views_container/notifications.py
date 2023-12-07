from apps.engine.views_container import (
    Notifications,
    ListAPIView,
    permissions,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveAPIView,
    LimitOffsetPagination,
    NotificationsSerializer,
    NotificationsCreateSerializer,
)


class NotificationsListAPIView(ListAPIView):
    queryset = Notifications.objects.all()
    serializer_class = NotificationsSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = LimitOffsetPagination


class NotificationsDetailAPIView(RetrieveAPIView):
    queryset = Notifications.objects.all()
    serializer_class = NotificationsSerializer
    permission_classes = [permissions.IsAuthenticated]


class NotificationsCreateAPIView(CreateAPIView):
    queryset = Notifications.objects.all()
    serializer_class = NotificationsCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    # override the default method create
    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)
        return super().perform_create(serializer)


class NotificationsUpdateAPIView(UpdateAPIView):
    queryset = Notifications.objects.all()
    serializer_class = NotificationsCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


class NotificationsDeleteAPIView(DestroyAPIView):
    queryset = Notifications.objects.all()
    serializer_class = NotificationsSerializer
    permission_classes = [permissions.IsAuthenticated]