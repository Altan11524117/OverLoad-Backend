from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'height', 'weight', 'fitness_goal', 'experience_level')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            height=validated_data.get('height'),
            weight=validated_data.get('weight'),
            fitness_goal=validated_data.get('fitness_goal', 'BULK'),
            experience_level=validated_data.get('experience_level', 'BEGINNER')
        )
        return user