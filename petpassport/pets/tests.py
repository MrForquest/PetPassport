import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from pets.models import Pet, PetAvatar

User = get_user_model()


class StaticURLTests(TestCase):
    def setUp(self):
        self.username = "test_user"
        self.password = "test_password"

        self.user = User.objects.create_user(
            username=self.username,
            password=self.password,
        )
        self.user.save()

        self.pet1 = Pet(
            name="PopaCat",
            birthday=datetime.date.today(),
            clade="Cat",
            owner=self.user,
        )
        avatar = PetAvatar(pet=self.pet1)
        self.pet1.avatar = avatar
        self.pet1.save()
        self.pet1.avatar.save()

        self.pet2 = Pet(
            name="PopaCat",
            birthday=datetime.date.today(),
            clade="Cat",
            owner=self.user,
        )
        avatar = PetAvatar(pet=self.pet2)
        self.pet2.avatar = avatar
        self.pet2.save()
        self.pet2.avatar.save()

    def tearDown(self) -> None:
        Pet.objects.all().delete()
        User.objects.all().delete()

        super(StaticURLTests, self).tearDown()

    def test_pets_list_endpoint(self) -> None:
        client = APIClient()
        access_jwt_url = reverse("v1:users:token_obtain_pair")
        response = self.client.post(
            access_jwt_url,
            data={"username": self.username, "password": self.password},
            format="json",
        )
        self.assertNotIn("detail", response.data)

        access_token = response.data["access"]

        client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
        response = client.get(
            reverse("v1:pets:pet-list"),
        )
        self.assertIn("pets", response.data)
