from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from backend.api.viewsets import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('users/', User.UsersList.as_view()),
    path('user/<str:pk>/', User.UserDetail.as_view()),

    path('pets/', Pets.PetsList.as_view()),
    path('pets/<str:pk>', Pets.PetDetail.as_view()),
    path('pets/<str:pk>/petMedicines/', Pets.PetMedicinesList.as_view()),
    # path('pets/petMedicines/', Pets.PetMedicinesList.as_view()),

    path('medicines/', Medicines.MedicineList.as_view()),
    # path('petMedicines/', Medicines.MedicineList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
