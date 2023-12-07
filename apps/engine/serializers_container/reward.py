from apps.engine.serializers_container import Reward, serializers


class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = "__all__"

    def create(self, validated_data):
        data = Reward.objects.create(**validated_data)
        return data
