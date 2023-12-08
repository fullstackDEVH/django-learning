from apps.engine.views_container import (
    SystemInformation,
    ListAPIView,
    permissions,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveAPIView,
    SystemInformationSerializer,
    LimitOffsetPagination
)


class SystemInformationListAPIView(ListAPIView):
    queryset = SystemInformation.objects.all()
    serializer_class = SystemInformationSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = LimitOffsetPagination


class SystemInformationDetailAPIView(RetrieveAPIView):
    queryset = SystemInformation.objects.all()
    serializer_class = SystemInformationSerializer
    permission_classes = [permissions.IsAuthenticated]


class SystemInformationCreateAPIView(CreateAPIView):
    queryset = SystemInformation.objects.all()
    serializer_class = SystemInformationSerializer
    permission_classes = [permissions.IsAuthenticated]


class SystemInformationUpdateAPIView(UpdateAPIView):
    queryset = SystemInformation.objects.all()
    serializer_class = SystemInformationSerializer
    permission_classes = [permissions.IsAuthenticated]


class SystemInformationDeleteAPIView(DestroyAPIView):
    queryset = SystemInformation.objects.all()
    serializer_class = SystemInformationSerializer
    permission_classes = [permissions.IsAuthenticated]