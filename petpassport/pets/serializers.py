import rest_framework.serializers

import pets.models


class PetListSerializer(rest_framework.serializers.HyperlinkedModelSerializer):
    avatar = rest_framework.serializers.SerializerMethodField()
    url = rest_framework.serializers.HyperlinkedIdentityField(
        view_name="pets:pet-detail"
    )

    class Meta:
        model = pets.models.Pet
        fields = [
            "url",
            pets.models.Pet.id.field.name,
            pets.models.Pet.name.field.name,
            "avatar",
        ]

    def get_avatar(self, obj):
        avatar = {
            "avatar_full": obj.avatar.image.url,
            "avatar_tmb": obj.avatar.image_tmb_url(),
        }
        return avatar


class PetDetailSerializer(
    rest_framework.serializers.HyperlinkedModelSerializer,
):
    owner = rest_framework.serializers.ReadOnlyField(
        source="owner.username", required=False
    )

    class Meta:
        model = pets.models.Pet
        fields = [
            pets.models.Pet.id.field.name,
            pets.models.Pet.name.field.name,
            pets.models.Pet.birthday.field.name,
            pets.models.Pet.clade.field.name,
            pets.models.Pet.breed.field.name,
            pets.models.Pet.description.field.name,
            pets.models.Pet.chip_number.field.name,
            pets.models.Pet.owner.field.name,
        ]


"""
class PetBaseDetailSerializer(rest_framework.serializers.Serializer):
    class Meta:
        fields = [
            pets.models.Pet.id.field.name,
            pets.models.Pet.name.field.name,
            pets.models.Pet.birthday.field.name,
            pets.models.Pet.clade.field.name,
            pets.models.Pet.breed.field.name,
            pets.models.Pet.description.field.name,
            pets.models.Pet.chip_number.field.name,
        ]


class PetRetrieveDetailSerializer(
    rest_framework.serializers.HyperlinkedModelSerializer,
    PetBaseDetailSerializer,
):
    owner = rest_framework.serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = pets.models.Pet
        fields = PetBaseDetailSerializer.Meta.fields + [
            pets.models.Pet.owner.field.name,
        ]


class PetCreateEditSerializer(
    rest_framework.serializers.ModelSerializer,
    PetBaseDetailSerializer,
):
    class Meta:
        model = pets.models.Pet
        fields = PetBaseDetailSerializer.Meta.fields
"""
