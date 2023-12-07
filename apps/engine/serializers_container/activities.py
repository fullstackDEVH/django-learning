from apps.engine.serializers_container import (
    Activities, serializers
)


class ActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activities
        fields = ["data"]

    def create(self, validated_data):
        user = Activities.objects.create(**validated_data)
        return user
