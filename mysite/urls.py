from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("inventory/", include("inventory.urls")),
    path("", lambda req: redirect("item_list")),
]
