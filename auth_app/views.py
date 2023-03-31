from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from auth_app.serializers import UserSerializer


UserModel = get_user_model()


class UserCreate(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        token, created = Token.objects.get_or_create(user=serializer.instance)

        user = UserModel.objects.get(username=serializer.data['username'])

        return Response(
            {
                'token': token.key,
                'user_id': user.id,
                'username': user.username,
            },
            status=status.HTTP_201_CREATED,
            headers=headers,
        )