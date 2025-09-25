from django.urls import path
from .import views
from .views import create_projet,list_projet, edit_projet,delete_projet,create_periode,edit_periode,delete_periode,create_stage,stage_list,stage_edit,stage_delete

app_name = "Administrations"

urlpatterns = [
    path("", views.index, name="main"),
    path("projet/create", create_projet, name="projet_create"),
    path('projet/liste', list_projet, name='list_projet'),
    path('projet/edit/<int:pk>', edit_projet, name="edit_projet"),
    path('projet/delete/<int:pk>', delete_projet, name="delete_projet"),
    path('periode/create',create_periode, name="create_periode"),
    path('/periode/edit/<int:pk>',edit_periode, name="edit_periode"),
    path('/periode/delete/<int:pk>',delete_periode, name="delete_periode"),
    path('/stage/create', create_stage, name="create_stage"),
    path('stage/liste', stage_list, name="stage_list"),
    path('stage/edit/<int:pk>', stage_edit, name="stage_edit"),
    path('stage/delete', stage_delete, name="stage_delete")
]