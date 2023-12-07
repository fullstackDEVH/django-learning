from apps.engine.serializers_container import Transaction, serializers


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"

    def create(self, validated_data):
        data = Transaction.objects.create(**validated_data)
        return data
