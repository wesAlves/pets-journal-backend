from rest_framework import viewsets

from backend import models
from backend.api import serializers

# Start to import views from viewsetsCases
from backend.api.viewsetsCases import userViewset as User
from backend.api.viewsetsCases import petViewset as Pets


# class PetsViweSet(viewsets.ModelViewSet):
#     serializer_class = serializers.PetsSerializer
#     queryset = models.Pets.objects.all()


class MedicinesViweSet(viewsets.ModelViewSet):
    serializer_class = serializers.MedicinesSerializer
    queryset = models.Medicines.objects.all()


class PetsMedicinesViweSet(viewsets.ModelViewSet):
    serializer_class = serializers.PetMedicinesSerializer
    queryset = models.PetMedicines.objects.all()


class VaccinesViweSet(viewsets.ModelViewSet):
    serializer_class = serializers.VaccinesSerializer
    queryset = models.Vaccines.objects.all()


class PetsVaccinesViweSet(viewsets.ModelViewSet):
    serializer_class = serializers.PetVaccinesSerializer
    queryset = models.PetVaccines.objects.all()
