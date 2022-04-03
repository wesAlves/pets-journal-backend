from django.db import models
from uuid import uuid4

# Create your models here.


class User(models.Model):
    id = models.UUIDField(default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, blank=False,
                              null=False, primary_key=True)
    password = models.CharField(max_length=200)

    created_at = models.DateField(auto_now_add=True)


class Medicines(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    laboratory = models.CharField(max_length=100)
    application_mode = models.CharField(max_length=50)


class Vaccines(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    laboratory = models.CharField(max_length=100)
    application_mode = models.CharField(max_length=50)


class PetVaccines(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    applicationDate = models.DateField()
    medicine = models.ForeignKey(Vaccines, on_delete=models.CASCADE)
    doses_per_application = models.IntegerField()
    time_between_doses = models.IntegerField()
    expires_on = models.DurationField()




class Pets(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    birthDate = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    weight = models.FloatField(max_length=100)
    weightUnity = models.CharField(max_length=100)
    imgURL = models.CharField(max_length=100)
    femaleOrMale = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # haveMedicines = models.ForeignKey(
    #     PetMedicines, on_delete=models.CASCADE, blank=True, null=True)
    # haveVaccines = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

class PetMedicines(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    applicationDate = models.DateField()
    doses_per_application = models.IntegerField()
    time_between_doses = models.IntegerField()
    expires_on = models.DurationField()
    medicine = models.ManyToManyField(Medicines)
    pet_owner = models.ForeignKey(Pets, on_delete=models.CASCADE,blank=True, null=True )