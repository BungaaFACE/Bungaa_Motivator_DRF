from rest_framework import generics
from users.models import User
from users.serializers import UserCreationSerializer, UserSerializerPrivateUpdate, UserSerializerPublic, UserSerializerPrivateDetails
from rest_framework import permissions

class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreationSerializer
    permission_classes = [permissions.AllowAny]


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializerPrivateUpdate
    
    def get_object(self):
        return self.request.user
    
class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializerPublic


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializerPrivateDetails
    
    def get_serializer_class(self):
        if self.get_object() == self.request.user:
            return UserSerializerPrivateDetails
        else:
            return UserSerializerPublic
    
    def get_object(self):
        pk = self.kwargs.get('pk', self.request.user.pk)
        return User.objects.get(pk=pk)