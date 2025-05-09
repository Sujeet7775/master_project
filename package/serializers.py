from rest_framework import serializers
from .models import Package

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'
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