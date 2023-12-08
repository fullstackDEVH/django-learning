from apps.engine.serializers_container import SystemInformation, serializers


class SystemInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemInformation
        fields = "__all__"

    def create(self, validated_data):
        data = SystemInformation.objects.create(**validated_data)
        return data