from rest_framework import serializers

class BaseAuditSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['created_by'] = user
        validated_data['updated_by'] = user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        user = self.context['request'].user
        validated_data['updated_by'] = user
        return super().update(instance, validated_data)
