from rest_framework import serializers
from backend import models


class PetsSerializer(serializers.ModelSerializer):
    haveMedicines = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    class Meta:
        model = models.Pets
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['id', 'email', 'name', 'password', 'created_at']
        # fields = "__all__"


class MedicinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Medicines
        fields = "__all__"


class VaccinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vaccines
        fields = "__all__"


class PetMedicinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PetMedicines
        fields = "__all__"


class PetVaccinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PetVaccines
        fields = "__all__"
