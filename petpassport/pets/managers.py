import django.contrib.auth.models
import django.db.models


class PetManager(django.db.models.Manager):
    def pet_list(self):
        return self.get_queryset().only(
            "id",
            "name",
            "owner__username",
        )
