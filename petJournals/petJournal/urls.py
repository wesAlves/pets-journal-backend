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
]

urlpatterns = format_suffix_patterns(urlpatterns)
