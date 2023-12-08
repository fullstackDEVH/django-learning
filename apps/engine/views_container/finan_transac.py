from apps.engine.views_container import (
    FinancialTransactions,
    ListAPIView,
    permissions,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveAPIView,
    FinancialTransactionsSerializer,
    LimitOffsetPagination
)


class FinancialTransactionsListAPIView(ListAPIView):
    queryset = FinancialTransactions.objects.all()
    serializer_class = FinancialTransactionsSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = LimitOffsetPagination


class FinancialTransactionsDetailAPIView(RetrieveAPIView):
    queryset = FinancialTransactions.objects.all()
    serializer_class = FinancialTransactionsSerializer
    permission_classes = [permissions.AllowAny]


class FinancialTransactionsCreateAPIView(CreateAPIView):
    queryset = FinancialTransactions.objects.all()
    serializer_class = FinancialTransactionsSerializer
    permission_classes = [permissions.IsAuthenticated]

    # override the default method create
    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)
        return super().perform_create(serializer)


class FinancialTransactionsUpdateAPIView(UpdateAPIView):
    queryset = FinancialTransactions.objects.all()
    serializer_class = FinancialTransactionsSerializer
    permission_classes = [permissions.IsAuthenticated]


class FinancialTransactionsDeleteAPIView(DestroyAPIView):
    queryset = FinancialTransactions.objects.all()
    serializer_class = FinancialTransactionsSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserFinancialTransactionsAPIView(ListAPIView):
    serializer_class = FinancialTransactionsSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = LimitOffsetPagination

    # override the default method create
    def get_queryset(self):
        # user_id = self.kwargs.get('user_id')
        queryset = FinancialTransactions.objects.filter(user_id=self.request.user)
        return queryset
