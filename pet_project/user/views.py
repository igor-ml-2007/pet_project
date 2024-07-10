from rest_framework import generics
from user.serializers import *
from rest_framework.permissions import IsAuthenticated


class UserRegisterAPIView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserCreateSerializer


class UserProfileAPIView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserProfileUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        try:
            user = Profile.objects.get(id=self.request.user.id)
            return user
        except Profile.DoesNotExist:
            return None


class UpdateProfileView(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
