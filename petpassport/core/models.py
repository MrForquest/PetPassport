import django.db.models
import django.utils.safestring
import sorl.thumbnail


class AbstractImageModel(django.db.models.Model):
    image = django.db.models.ImageField(
        upload_to="images/",
        verbose_name="image",
        default="default/no-image.jpg",
    )

    @property
    def get_image_300x300(self):
        return sorl.thumbnail.get_thumbnail(
            self.image, "300x300", crop="center", quality=51
        )

    def image_tmb_html(self):
        if self.image:
            thumb = self.get_image_300x300
            return django.utils.safestring.mark_safe(
                f'<img src="{thumb.url}" width="200rem;">'
            )

    def image_tmb_url(self):
        if self.image:
            thumb = self.get_image_300x300
            return thumb.url

    class Meta:
        verbose_name = "image"
        verbose_name_plural = "images"
        abstract = True

    def __str__(self):
        if hasattr(self, "item"):
            return f"Image {self.item.name}"
        else:
            return "Image"

    image_tmb_html.short_description = "preview"
    image_tmb_html.allow_tags = True
