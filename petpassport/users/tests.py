import datetime

import rest_framework.status
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth.hashers import make_password

from pets.models import Pet, PetAvatar

User = get_user_model()


class UserAPITests(TestCase):
    def setUp(self):
        pass

    def tearDown(self) -> None:
        Pet.objects.all().delete()
        User.objects.all().delete()

        super(UserAPITests, self).tearDown()

    def test_create_user_endpoint(self) -> None:
        client = APIClient()
        data = {
            "username": "TestUsername",
            "password": "TestPassword",
            "email": "TestEmail@test.test",
        }
        num_users = User.objects.count()
        create_url = reverse("v1:users:user-create")
        response = client.post(create_url, data=data)
        self.assertEqual(
            response.status_code,
            rest_framework.status.HTTP_201_CREATED,
            msg=response.data,
        )

        self.assertEqual(num_users + 1, User.objects.count())

    def test_upload_avatar_endpoint(self) -> None:
        creds = {
            "username": "TestUsername",
            "password": "TestPassword",
        }
        data = {
            "username": creds["username"],
            "password": make_password(creds["password"]),
            "email": "TestEmail@test.test",
            "is_active": True,
        }
        user = User(**data)
        user.save()

        client = APIClient()
        self.authorization_client(client, creds)

        user_detail_url = reverse(
            "v1:users:user-detail", kwargs={"pk": user.id}
        )
        response = client.patch(
            user_detail_url,
            data={
                "avatar": {
                    "avatar_full": "obj.avatar.image.url",
                    "avatar_tmb": "obj.avatar.image_tmb_url()",
                }
            },
        )
        print(response.data)
        # TODO: test_upload_avatar_endpoint
        # self.assertEqual(1, 0)

    def authorization_client(self, client, credentials):
        access_jwt_url = reverse("v1:users:token_obtain_pair")
        response = self.client.post(
            access_jwt_url,
            data={
                "username": credentials["username"],
                "password": credentials["password"],
            },
            format="json",
        )
        self.assertNotIn("detail", response.data, msg=response.data)
        access_token = response.data["access"]

        client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")

        return response.data

    def test_authorization(self):
        creds = {
            "username": "TestUsername",
            "password": "TestPassword",
        }
        data = {
            "username": creds["username"],
            "password": make_password(creds["password"]),
            "email": "TestEmail@test.test",
            "is_active": True,
        }
        user = User(**data)
        user.save()

        client = APIClient()
        tokens = self.authorization_client(client, creds)

        access_token = tokens["access"]
        verify_token_url = reverse("v1:users:token_verify")
        response = client.post(verify_token_url, data={"token": access_token})

        self.assertEqual(
            response.status_code,
            rest_framework.status.HTTP_200_OK,
            msg=response.data,
        )
