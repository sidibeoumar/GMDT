from django.shortcuts import render,redirect, HttpResponse,get_object_or_404
from .forms import UserForm,CreateEncadreurForm
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .models import User
from Administrations.models import Periode,Stag
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import AffecteStageform

# Create your views here.
def index(request):
    stagiaires = User.objects.filter(role='demandeur')
    periodes = Periode.objects.all()
    demandes_count= User.objects.filter(status="traitement_encour").count()
    valide_count= User.objects.filter(status="valid").count()
    print(stagiaires)
    return render(request, 'dashbord.html', {
        'stagaires':stagiaires, 
        "periodes":periodes,
        "demandes_count":demandes_count,
        "valide_count":valide_count
        })


def register_user(request):
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():            
                user = form.save(commit=False)                        
                user.set_password(form.cleaned_data['password1'])
                user.save() 
                subject = "Demande prise en compte"
                message = (
                        f"Bonjour {user.username},\n\n"
                        "Nous vous informons que votre demande a été prise en compte.\n"
                        "Veuillez patienter, une notification vous sera envoyée "
                        "pour vous informer de l'acceptation de votre stage.\n\n"
                        "Cordialement,\nL'équipe G_STAGE"
                    )
                from_email = settings.DEFAULT_FROM_EMAIL
                recipient_list = [user.email]
                send_mail(subject, message, from_email, recipient_list, fail_silently=False)
                messages.success(request, "Votre demande a été prise en compte. Un email vous a été envoyé.")    
                 # ✅ Tentative d'envoi de l'email
                try:
                    subject = "Demande prise en compte"
                    message = (
                            f"Bonjour {user.username},\n\n"
                            "Nous vous informons que votre demande a été prise en compte.\n"
                            "Veuillez patienter, une notification vous sera envoyée "
                            "pour vous informer de l'acceptation de votre stage.\n\n"
                            "Cordialement,\nL'équipe G_STAGE"
                        )
                    from_email = settings.DEFAULT_FROM_EMAIL
                    recipient_list = [user.email]
                    send_mail(subject, message, from_email, recipient_list, fail_silently=False)
                    
                except Exception as e:
                    

                    messages.success(request, "Votre demande a été prise en compte. Un email vous a été envoyé.")

                    # ✅ Dans tous les cas, on redirige vers login
                return redirect('Accounts:login_user')                
        
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
                if user.role == "demandeur":                    
                    messages.success(request, f"Bienvenue {user.username} 👋")                    
                elif user.role == 'Encadreur':
                    return redirect('Accounts:encadreur_dash')
                else:
                    return redirect('Accounts:index')  # ✅ redirige vers la page d’accueil
            else:
                messages.error(request, "Nom d’utilisateur ou mot de passe invalide.")
        else:
            messages.error(request, "Erreur dans le formulaire.")
    else:
        form = AuthenticationForm()

    return render(request, 'Account/login_user.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('Accounts:login_user')

def create_encadreur(request):
    if request.method == 'POST':  # ✅ 'Post' → 'POST'
        form = CreateEncadreurForm(request.POST, request.FILES)
        if form.is_valid():
            raw_password = form.cleaned_data.get("password1")
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")

            encadreur = form.save(commit=False)  # ✅ 'comit' → 'commit'
            encadreur.role = 'Encadreur'
            encadreur.status = 'Encadreur'  # ✅ 'statuts' → 'status'
            encadreur.save()

            # ✅ Envoi email
            subject = "Création de votre compte G_STAGE"
            message = (
                f"Bonjour {encadreur.first_name} {encadreur.last_name},\n\n"
                f"Un compte encadreur a été créé pour vous sur G_STAGE.\n\n"
                f"Identifiants de connexion :\n"
                f"👤 Nom d’utilisateur : {username}\n"
                f"🔑 Mot de passe : {raw_password}\n\n"
                f"Veuillez vous connecter et changer votre mot de passe dès votre première connexion.\n\n"
                f"Cordialement,\nL'équipe G_STAGE."
            )          
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )

            messages.success(request, "✅ L'encadreur a été créé avec succès et un email lui a été envoyé.")
            return redirect('Accounts:list_encadreur')  # 🔁 redirection après succès
    else:
        form = CreateEncadreurForm()

    return render(request, 'Encadreur/create_encadreur.html', {'form': form})

def list_encadeur(request):
    encadreurs = User.objects.filter(role='Encadreur')
    return render(request, 'Encadreur/list_encadreur.html', {'encadreurs':encadreurs})

def update_encadreur(request, pk):
    encadreur = User.objects.get(pk=pk)
    form = CreateEncadreurForm(instance=encadreur)
    if request.method == 'POST':
        form = CreateEncadreurForm(request.POST, instance=encadreur)
        if form.is_valid():
            form.save()
            return redirect('Accounts:list_encadreur')
    return render(request, 'Encadreur/')
    
def delete_encadreur(request, pk):
    encadreur = User.objects.get(pk=pk)
    if request.method == 'POST':
        encadreur.delete()
        return redirect('Accounts:list_encadeur')
    return render(request, 'Encadreur/list_encadreur.html', {'encadreur':encadreur  })

@login_required
def reject_user_demande(request, pk):
    user = get_object_or_404(User, pk=pk)

    username = user.username
    mail = user.email

    user.status="rejet"

   
    try:

        # envoie Mail 
        subject = "Réponse à votre demande de stage"
        message = (
            f"Bonjour {username},\n\n"
            f"Nous vous remercions pour l'intérêt que vous avez porté à notre programme de stage.\n\n"
            f"Après examen de votre demande, nous sommes au regret de vous informer qu’elle n’a pas été retenue pour cette session.\n\n"
            f"Nous vous encourageons vivement à postuler à nouveau lors des prochaines ouvertures.\n\n"
            f"Nous vous souhaitons plein succès dans vos démarches futures.\n\n"
            f"Cordialement,\nL’équipe MDT-informatique"

        )
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            mail,
            fail_silently=False,
        )
        messages.success(request, f"L'utilisateur {username} a été rejeté et un email a été envoyé ✅")
    except Exception as e :
        messages.warning(request, f"L'utilisateur {username} a été rejeté, mais l'envoi de l'email a échoué ⚠️")
    # suppression du compte de user
    user.delete()

    return redirect('Accounts:index')

@login_required
def stage_validation(request, pk):
    user = get_object_or_404(User, pk=pk)

    if user.role !="demandeur":
        messages.warning(request, "cet utilisateur n'est pas un demandeur ❌")
        return redirect("Accounts:index")
    
    if request.method == 'POST':
        form = AffecteStageform(request.POST, instance=user)
        if form.is_valid():
            stagiaire = form.save(commit=False)
            stage = form.cleaned_data['stage']

            stagiaire.role = "stagiaire"
            stagiaire.status = "valid"
            stagiaire.stage = stage
            stagiaire.save()

            # récupération des infos du stage
            stage = stagiaire.stage
            print(stage)
            projet = stage.projet
            debut = stage.periode.date_debut
            fin = stage.periode.date_fin
            try:
                # Envoi de mail
                subject = "Validation de votre stage ✅"
                message = (
                    f"Bonjour Mr{stagiaire.first_name},\n\n"
                    f"Votre stage a été validé avec succès.\n\n"
                    f"Détails du stage :\n"
                    f"Projet : {projet}\n"
                    f"Date de début : {debut}\n"
                    f"Date de fin : {fin}\n\n"
                    f"Nous vous souhaitons plein succès dans cette expérience.\n\n"
                    f"Cordialement,\nL'équipe MDT-informatique"

                )
                send_mail(
                    subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    [stagiaire.email],
                    fail_silently=False,
                )
            except Exception as e:
                messages.success(request, f"{stagiaire.first_name}  {stagiaire.last_name} est validé et affecté au stage {stagiaire.stage.projet} ✅")

        return redirect('Accounts:stage_valid')
            
    else:
        form = AffecteStageform(instance=user)
    
    return render(request, "Account/affecter_stage.html", {"form":form, "user":user})


def stage_valid(request):
    stagesvalid = User.objects.filter(status="valid")
    return render(request, 'Account/stage_valid.html', {'stagesvalid':stagesvalid})

@login_required
def encadreur_dash(request):
    encadreur = request.user
    # Récupération des stagiaires affectés à cet encadreur
    stagiaires = User.objects.filter(role='stagiaire', encadreur=encadreur).select_related('stage')


    # Crée une liste de tuples (stagiaire, rapport)
    stagiaires_rapports = []
    for st in stagiaires:
        if st.stage:
            if st.stage.rapport_stage:
                stagiaires_rapports.append((st, st.stage.rapport_stage))
            else:
                stagiaires_rapports.append((st, "Pas de rapport associé"))
        else:
            stagiaires_rapports.append((st, "Pas de stage affecté"))
    return render(request, 'Account/encadreur_dash.html', {
        "encadreur":encadreur,
        "stagiaires":stagiaires
    })
    
   
    
