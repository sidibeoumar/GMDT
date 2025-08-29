from django.shortcuts import render,redirect, HttpResponse,get_object_or_404
from .forms import UserForm
from django.contrib import messages
from .models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def register_user(request):
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():            
             user = form.save(commit=False)
             user.set_password(form.cleaned_data['password'])
             user.save()  
             messages.success(request, "La demande a été prise en compte")
        return redirect('logout_user')
    else:
        form = UserForm()
    
    return render(request, 'Account/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)   # ✅ connexion de l’utilisateur
                messages.success(request, f"Bienvenue {user.username} 👋")
                return redirect('index')  # ✅ redirige vers la page d’accueil
            else:
                messages.error(request, "Nom d’utilisateur ou mot de passe invalide.")
        else:
            messages.error(request, "Erreur dans le formulaire.")
    else:
        form = AuthenticationForm()

    return render(request, 'Account/login_user.html', {'form': form})