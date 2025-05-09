from rest_framework import serializers
from .models import District

class DistrictAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['id', 'package', 'district_name', 'district_code', 'created_by', 'updated_by', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_by', 'updated_by', 'created_at', 'updated_at']

    def create(self, validated_data):
        # Automatically set the created_by and updated_by fields to the logged-in user
        user = self.context['request'].user
        validated_data['created_by'] = user
        validated_data['updated_by'] = user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Automatically update the updated_by field to the logged-in user
        user = self.context['request'].user
        validated_data['updated_by'] = user
        return super().update(instance, validated_data)