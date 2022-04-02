from rest_framework.response import Response
from rest_framework.decorators import APIView

from backend.models import Medicines
from backend.api.serializers import MedicinesSerializer


class MedicineList(APIView):

    def get(self, request, format=None):
        medicines = Medicines.objects.all()
        serializer = MedicinesSerializer(medicines, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MedicinesSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
