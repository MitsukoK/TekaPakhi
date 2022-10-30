from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("", include("landing.urls")),
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("user/", include("userapp.urls")),
]
