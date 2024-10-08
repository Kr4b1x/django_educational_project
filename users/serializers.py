from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model.
    """
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        """
        Create and save a new user.
        """
        user = User(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    def update(self, instance, validated_data):
        """
        Update an existing user.
        """
        instance.set_password(validated_data["password"])
        instance.save()
        return instance
