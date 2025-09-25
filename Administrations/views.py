from django.shortcuts import render, redirect,get_list_or_404
from Administrations.forms import Projetform,PeriodeForm,StagForm
from .models import Projet,Periode,Stag

# Create your views here.
def index(request):
    return render(request,  'index.html')

def create_projet(request):
    projet = Projetform()
    if request.method == 'POST':
        form = Projetform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Administrations:list_projet')
    else:
        form = Projetform()
    return render(request, 'projet/projet_create.html',{'form':projet})

def list_projet(request):
    projects = Projet.objects.all()
    return render(request, 'projet/list_projet.html', {'projets':projects})

def delete_projet(request, pk):
    projet = get
    # projet = Projet.objects.get(pk=pk)
    # form = Projetform(instance=projet)
    if request.method == 'POST':
        form = Projetform(request.POST, instance=projet)
        if form.is_valid():
            form.save()
            return redirect('Administrations:list_projet')
        return render(request, 'projet/')

def edit_projet(request, pk):
    projet = get_list_or_404(Projet, pk=pk)
    # projet = Projet.objects.get(pk=pk)
    # form = Projetform(instance=projet)
    if request.method == 'POST':
        form = Projetform(request.POST, instance=projet)
        if form.is_valid():
            form.save()
            return redirect('Administrations:list_projet')
    else:
        form = Projetform(instance=projet)
    return render(request, 'projet/projet_create.html', {'form':form})

def delete_projet(request, pk):
    projet = Projet.objects.get(pk=pk)
    if request.method == 'POST':
        projet.delete()
        return redirect('Administrations:list_projet')
    return render(request, 'projet/list_projet.html', {'projet':projet})

def create_periode(request):
    form = PeriodeForm()
    if request.method == 'POST':
        form = PeriodeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Accounts:index')
    else:
        form = PeriodeForm()
    return render(request, 'Periode/periode_create.html', {'form':form})

def edit_periode(request, pk):
    projet = Periode.objects.get(pk=pk)
    form = PeriodeForm(instance=projet)
    if request.method == 'POST':
        form = PeriodeForm(request.POST, instance=projet)
        if form.is_valid():
            form.save()
        return redirect('Accounts:index')
    else:
        form = PeriodeForm(instance=projet)
    return render(request, 'Periode/periode_create.html', {'form':form})


def delete_periode(request, pk):
    projet = Projet.objects.get(pk=pk)
    if request.method == 'POST':
        projet.delete()
        return redirect('Administrations:list_periode')
    return render(request, 'projet/list_periode.html', {'projet':projet})

def create_stage(request):
    form = StagForm()
    if request.method == 'POST':
        form = StagForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Administrations:list_stag')
    else:
        form = StagForm()
    return render(request, "Stage/create_stage.html", {'form':form})

def stage_list(request):
    Stages = Stag.objects.all()
    return render(request, 'Stage/stage_liste.html', {'stages':Stages})

def stage_edit(request, pk):
    stage = Stag.objects.get(pk=pk)
    form = StagForm(instance=stage)
    if form.method == 'POST':
        form = StagForm(request.POST, instance=stage)
        if form.is_valid():
            form.save()
        return redirect('Administrations:stage_list')
    else:
        form = form = StagForm(instance=stage)
    return render(request, 'Stage/create_stage.hml')    

def stage_delete(request, pk):
    form = Stag.objects.get(pk=pk)
    if request.method == 'POST':
        form.delete()
        return redirect('Administrations:list_stag')
    return render('Stage/stage_delete.html', {'form':form})

            