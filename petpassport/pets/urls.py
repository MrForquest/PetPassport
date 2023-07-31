from django.urls import path

import pets.views

app_name = "pets"

urlpatterns = [
    path("pets/", pets.views.PetList.as_view(), name="pet-list"),
    path("pets/<int:pk>/", pets.views.PetDetail.as_view(), name="pet-detail"),
]
