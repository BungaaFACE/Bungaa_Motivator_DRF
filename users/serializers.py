from rest_framework import serializers
from users.models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class UserCreationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            first_name='',
            last_name='',
            is_active=True,
            is_staff=False,
            is_superuser=False,
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = UserModel
        fields = ["email", "password"]

class UserSerializerPrivateUpdate(serializers.ModelSerializer):
    
    class Meta:
        model = User
        exclude = ['password', 'is_superuser', 'is_staff', 'email', 'is_active', 'groups', 'user_permissions']



class UserSerializerPrivateDetails(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'
        
        
class UserSerializerPublic(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('password', 'last_name')
        

