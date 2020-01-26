from django.urls import path

from inventory import views

urlpatterns = [
    path("", views.item_list, name="item_list"),
    path("<int:pk>/", views.item_read, name="item_read"),
    path("create/", views.item_create, name="item_create"),
    path("update/<int:pk>/", views.item_update, name="item_update"),
]