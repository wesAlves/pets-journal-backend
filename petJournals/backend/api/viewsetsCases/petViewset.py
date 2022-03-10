from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import APIView

from backend.models import Pets
from backend.api.serializers import PetsSerializer


class PetsList(APIView):
    def get(self, request, format=None):
        pets = Pets.objects.all()
        serializer = PetsSerializer(pets, many=True)

        return Response(serializer.data)

    def post(self, request, fromat=None):
        serializer = PetsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PetDetail(APIView):
    def get_objects(self, pk):
        try:
            return Pets.objects.get(pk=pk)
        except Pets.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        pet = self.get_objects(pk)
        serializer = PetsSerializer(pet)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        pet = self.get_objects(pk)
        serializer = PetsSerializer(pet, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        pet = self.get_objects(pk)
        pet.delete()

        return Response(status=status.HTTP_400_BAD_REQUEST)
