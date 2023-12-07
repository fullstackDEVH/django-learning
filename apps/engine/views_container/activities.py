from apps.engine.views_container import (
    Activities,
    ListAPIView,
    permissions,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveAPIView,
    ActivitiesSerializer,
    LimitOffsetPagination
)


class ActivitiesListAPIView(ListAPIView):
    queryset = Activities.objects.all()
    serializer_class = ActivitiesSerializer
    permission_classes = [permissions.AllowAny]


class ActivitiesDetailAPIView(RetrieveAPIView):
    queryset = Activities.objects.all()
    serializer_class = ActivitiesSerializer
    permission_classes = [permissions.AllowAny]


class ActivitiesCreateAPIView(CreateAPIView):
    queryset = Activities.objects.all()
    serializer_class = ActivitiesSerializer
    permission_classes = [permissions.IsAuthenticated]

    # override the default method create
    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)
        return super().perform_create(serializer)


class ActivitiesUpdateAPIView(UpdateAPIView):
    queryset = Activities.objects.all()
    serializer_class = ActivitiesSerializer
    permission_classes = [permissions.IsAuthenticated]


class ActivitiesDeleteAPIView(DestroyAPIView):
    queryset = Activities.objects.all()
    serializer_class = ActivitiesSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserActivitiesAPIView(ListAPIView):
    serializer_class = ActivitiesSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = LimitOffsetPagination

    # override the default method create
    def get_queryset(self):
        # user_id = self.kwargs.get('user_id')
        queryset = Activities.objects.filter(user_id=self.request.user)
        return queryset
