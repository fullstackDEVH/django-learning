from apps.engine.views_container import (
    Transaction,
    ListAPIView,
    permissions,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveAPIView,
    TransactionSerializer,
    LimitOffsetPagination
)


class TransactionListAPIView(ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = LimitOffsetPagination


class TransactionDetailAPIView(RetrieveAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.AllowAny]


class TransactionCreateAPIView(CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    # override the default method create
    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)
        return super().perform_create(serializer)


class TransactionUpdateAPIView(UpdateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]


class TransactionDeleteAPIView(DestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]