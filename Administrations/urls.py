from django.urls import path
from .import views
from .views import create_projet,list_projet, edit_projet,delete_projet

urlpatterns = [
    path("", views.index, name="index"),
    path("projet/create", create_projet, name="projet_create"),
    path('projet/liste', list_projet, name='list_projet'),
    path('projet/edit/<int:pk>', edit_projet, name="edit_projet"),
    path('projet/delete/<int:pk>', delete_projet, name="delete_projet")

]