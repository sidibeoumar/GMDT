from django.shortcuts import render, redirect
from .forms import Projetform
from .models import Projet

# Create your views here.
def index(request):
    return render(request,  'index.html')

def create_projet(request):
    projet = Projetform()
    if request.method == 'POST':
        form = Projetform(request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_projet)
    else:
        form = Projetform()
    return render(request, 'projet/projet_create.html',{'form':form})

def list_projet(request):
    projects = Projet.objects.all()
    return render(request, 'projet/list_projet.html', {'projets':projects})

def delete_projet(request, pk):
    projet = Projet.objects.get(pk=pk)
    form = Projetform(instance=projet)
    if request.method == 'POST':
        form = Projetform(request.POST, instance=projet)
        if form.is_valid():
            form.save()
            return redirect('list_projet')
        return render(request, 'projet/')

def edit_projet(request, pk):
    projet = Projet.objects.get(pk=pk)
    form = Projetform(instance=projet)
    if request.method == 'POST':
        form = Projetform(request.POST, instance=projet)
        if form.is_valid():
            form.save()
        return redirect('list_projet')
    return render(request, 'projet/projet_create.html', {'form':form})

def delete_projet(request, pk):
    projet = Projet.objects.get(pk=pk)
    if request.method == 'POST':
        projet.delete()
        return redirect(list_projet)
    return render(request, 'projet/list_projet.html', {'projet':projet})
    
            