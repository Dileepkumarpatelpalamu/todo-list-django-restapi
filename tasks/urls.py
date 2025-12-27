from django.urls import path, include

urlpatterns = [
    path("api/", include("tasks.api.urls")),
    path("", include("tasks.web.urls")),
]