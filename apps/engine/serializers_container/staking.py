from apps.engine.serializers_container import Staking, serializers


class StakingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staking
        fields = "__all__"

    def create(self, validated_data):
        data = Staking.objects.create(**validated_data)
        return data