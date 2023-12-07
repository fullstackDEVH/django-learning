from apps.engine.serializers_container import UserStaking, serializers


class UserStakingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStaking
        fields = "__all__"

    def create(self, validated_data):
        data = UserStaking.objects.create(**validated_data)
        return data
