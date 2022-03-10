from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import APIView

from backend.models import User
from backend.api.serializers import UserSerializer


class UsersList(APIView):  # To use in that way need to refactory the urls files to chante
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):

    def get_objects(self, pk):
        try:
            return User.objects.get(pk=pk)

        except User.DoesNotExist:
            return Http404

    # need to pass email as query parm because email is the primary key
    def get(self, request, pk, format=None):
        user = self.get_objects(pk)
        serializer = UserSerializer(user)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_objects(pk)
        serializer = UserSerializer

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_objects(pk)
        user.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
