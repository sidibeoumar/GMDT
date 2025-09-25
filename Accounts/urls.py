from django.urls import path
from .views import register_user, login_user,index,logout_user,create_encadreur,list_encadeur,update_encadreur,delete_encadreur,stage_validation,reject_user_demande,stage_valid,encadreur_dash
from . import views 


app_name = "Accounts"

urlpatterns = [
    path('account/register', register_user, name='register_user'),
    path('account/login', login_user, name='login_user'),
    # path('account/dashbord', Dashbord, name="Dashbord"),
    path('/dashbord', index, name="index"),
    path('account/logout', logout_user, name="logout_user"),
    path('encadreur/create',create_encadreur, name="create_encadreur"),
    path('encadreur/list', list_encadeur, name="list_encadeur"),
    path('encadreur/update/<int:pk>', update_encadreur, name="update_encadreur"),
    path('encadreur/delete/<int:pk>', delete_encadreur, name="delete_encadreur"),
    path('affecter/stage/<int:pk>',stage_validation, name="stage_validation"),
    path('/stage/rejet/<int:pk>', reject_user_demande, name="reject_user_demande"),
    path('accounts/stagevalid', stage_valid, name="stage_valid"),
    path('dashencadreur/', encadreur_dash, name='encadreur_dash'),
]