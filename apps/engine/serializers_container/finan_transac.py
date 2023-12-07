from apps.engine.serializers_container import FinancialTransactions, serializers


class FinancialTransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialTransactions
        fields = "__all__"

    def create(self, validated_data):
        data = FinancialTransactions.objects.create(**validated_data)
        return data
