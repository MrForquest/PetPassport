import django.contrib.admin

import pets.models


class PetAvatarModelInline(django.contrib.admin.StackedInline):
    model = pets.models.PetAvatar
    can_delete = False
    readonly_fields = ("image_tmb_html",)
    fk_name = "pet"


@django.contrib.admin.register(pets.models.Pet)
class PetAdmin(django.contrib.admin.ModelAdmin):
    list_display = (
        pets.models.Pet.name.field.name,
        "owner_username",
    )
    inlines = (PetAvatarModelInline,)

    def owner_username(self, obj):
        return obj.owner.username
