from apps.engine.serializers_container import (
    Notifications, serializers
)


class NotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = "__all__"


class NotificationsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = ["data"]

    def create(self, validated_data):
        data = Notifications.objects.create(**validated_data)
        return data
