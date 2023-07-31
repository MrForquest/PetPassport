from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.urlpatterns import format_suffix_patterns

from petpassport.swagger import APISchemeGenerator

schema_view = get_schema_view(
    openapi.Info(
        title="Pets API",
        default_version="v1",
        description="Test description",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    generator_class=APISchemeGenerator,
)

docs_patterns = [
    path(
        r"swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        r"redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]

api_urls = [
    path("", include("users.urls")),
    path("", include("pets.urls")),
    path("docs/", include(docs_patterns)),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r"api/v1/", include((api_urls, "api_urls"), namespace="v1")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (path("__debug__/", include(debug_toolbar.urls)),)

#    path("auth/", include("rest_framework.urls", namespace="rest_framework")),
urlpatterns = format_suffix_patterns(urlpatterns)
