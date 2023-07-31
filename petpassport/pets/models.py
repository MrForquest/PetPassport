import django.db.models

import core.models
import users.models
from pets.managers import PetManager


def pet_avatar_directory_path(instance, filename):
    img_type = filename.split(".")[-1]
    return f"avatars/pet_avatar_{instance.pet.id}.{img_type}"


class Pet(django.db.models.Model):
    objects = PetManager()
    name = django.db.models.fields.CharField(
        "name",
        max_length=50,
    )
    birthday = django.db.models.fields.DateField("birthday")

    clade = django.db.models.fields.CharField(
        "family",
        max_length=100,
    )

    breed = django.db.models.fields.CharField(
        "breed",
        max_length=100,
        blank=True,
        null=True,
    )

    description = django.db.models.fields.CharField(
        "description",
        max_length=300,
        blank=True,
        null=True,
    )
    chip_number = django.db.models.fields.CharField(
        "chip number",
        max_length=20,
        blank=True,
        null=True,
    )

    owner = django.db.models.ForeignKey(
        users.models.User,
        on_delete=django.db.models.CASCADE,
        related_name="pets",
    )

    class Meta:
        verbose_name = "pet"
        verbose_name_plural = "pets"

    # def clean(self, *args, **kwargs) -> None:
    #     print("!" * 20)
    #     try:
    #         self.avatar
    #     except Pet.avatar.RelatedObjectDoesNotExist:
    #         avatar = PetAvatar(pet=self)
    #         self.avatar = avatar
    #     super(Pet, self).clean()

    def save(self, *args, **kwargs):
        self.full_clean()

        return super(Pet, self).save(*args, **kwargs)

    def __str__(self):
        return f"Pet {self.name}"


class PetAvatar(core.models.AbstractImageModel):
    image = django.db.models.ImageField(
        upload_to=pet_avatar_directory_path,
        verbose_name="image",
        default="default/no-image.jpg",
    )
    pet = django.db.models.OneToOneField(
        Pet,
        django.db.models.CASCADE,
        related_name="avatar",
    )

    class Meta:
        verbose_name = "pet avatar"
        verbose_name_plural = "pet avatars"
