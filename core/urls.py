
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
    title="Geeks Blog",
    default_version="v1",
    description="Пробуем REST",
    terms_of_service="",
    contact=openapi.Contact(email="test@test.com"),
    license=openapi.License(name="No license"),
     
    ),
    public=True,
    permission_classes=(
        [
            permissions.AllowAny,
        ]
    ),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0),name="schema-swagger-ui"),
    path("", include("posts.urls")),

    path("users/", include("django.contrib.auth.urls")),
    path("", include("users.urls")),

]
