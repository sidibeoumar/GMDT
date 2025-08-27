from django.urls import path
from .import views
from .views import create_projet,list_projet

urlpatterns = [
    path("", views.index, name="index"),
    path("projet/create", create_projet, name="projet_create"),
    path('projet/liste', list_projet, name='list_projet'),

]