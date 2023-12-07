from apps.engine.serializers_container import (
    Activities, serializers
)

class ActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activities
        fields = "__all__"


class ActivitiesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activities
        fields = ["data"]

    def create(self, validated_data):
        data = Activities.objects.create(**validated_data)
        return data
