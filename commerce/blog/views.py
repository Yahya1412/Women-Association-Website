from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from django.shortcuts import redirect
from .models import  Event, Participant
from django.core.paginator import Paginator
import json
from django.http import JsonResponse, HttpResponse
import csv
from datetime import datetime


def index(request):
    event = Event.objects.all()
    event = Event.objects.order_by('date')
    paginator = Paginator(event,7)
    page_number=request.GET.get('page')
    page_obj=Paginator.get_page(paginator, page_number)
    context={
        'event': event,
        'page_obj': page_obj,
    }
    return render(request, 'shop/blog.html', context)

def ajouter_blog(request):
    event = Event.objects.all()

    context = {
        'event': event,
        'values': request.POST
    }

    if request.method == 'GET':
        return render(request, 'shop/ajouter_blog.html', context)

    if request.method == 'POST':
        nomeven = request.POST['nomeven']
        if not nomeven:
            messages.warning(request, 'Le champ Nom évenement est nécessaire')
            return render(request, 'shop/ajouter_blog.html', context)

        desceven = request.POST['desceven']
        if not desceven:
            messages.warning(request, 'Le champ description évenement est nécessaire')
            return render(request, 'shop/ajouter_blog.html', context)

        localisation = request.POST['localisation']
        if not localisation:
            messages.warning(request, 'Le champ Localisation événement est nécessaire')
            return render(request, 'shop/ajouter_blog.html', context)
        date = request.POST['date']
        if not date:
            messages.warning(request, 'Le champ Date évenement est nécessaire')
            return render(request, 'shop/ajouter_blog.html', context)

        Event.objects.create(
            nomeven=nomeven,
            desceven=desceven,
            localisation=localisation,
            date=date,
        )

        messages.success(request, 'Blog enregistrée avec succès')
        return redirect('blog')

def blog_edit(request, id):
    event = Event.objects.get(pk=id)
    context ={
        'event': event,
    }

    if request.method == 'GET':
        return render(request, 'shop/modifier_blog.html', context)

    if request.method == 'POST':
        nomeven = request.POST['nomeven']
        if not nomeven:
            messages.warning(request, 'Le champ Nom évenement est nécessaire')
            return render(request, 'shop/modifier_blog.html', context)

        desceven = request.POST['desceven']
        if not desceven:
            messages.warning(request, 'Le champ Description évenement est nécessaire')
            return render(request, 'shop/modifier_blog.html', context)

        localisation = request.POST['localisation']
        if not localisation:
            messages.warning(request, 'Le champ La localisation évenement est nécessaire')
            return render(request, 'shop/modifier_blog.html', context)
        date = request.POST['date']
        if not date:
            messages.warning(request, 'Le champ Date évenement est nécessaire')
            return render(request, 'shop/modifier_blog.html', context)

        event.nomeven = nomeven
        event.desceven = desceven
        event.localisation = localisation
        event.date= date
        event.save()

        messages.success(request, 'Modification enregistrée avec succès')
        return redirect('blog')
    
def supprimer_blog(request, id):
    compte = Event.objects.get(pk=id)
    compte.delete()
    messages.success(request,'Evenement supprimer avec succés')
    return redirect('blog')
def participer(request):
    event = Event.objects.all()
    part = Participant.objects.all()

    context = {
        'event': event,
        'part': part,
        'values': request.POST
    }

    if request.method == 'GET':
        return render(request, 'shop/participer.html', context)

    if request.method == 'POST':
        nom = request.POST['nom']
        if not nom:
            messages.warning(request, 'Le champ Nom est nécessaire')
            return render(request, 'shop/participer.html', context)

        prenom = request.POST['prenom']
        if not prenom:
            messages.warning(request, 'Le champ Prénom est nécessaire')
            return render(request, 'shop/participer.html', context)
        sexe = request.POST['sexe']
        if not sexe:
            messages.warning(request, 'Le champ Sexe du Participant(e) est nécessaire')
            return render(request, 'shop/participer.html', context)

        profession = request.POST['profession']
        if not profession:
            messages.warning(request, 'Le champ Profession est nécessaire')
            return render(request, 'shop/participer.html', context)
        date_naissance = request.POST['date_naissance']
        if not date_naissance:
            messages.warning(request, 'Le champ Date de Naissance est nécessaire')
            return render(request, 'shop/participer.html', context)

        Participant.objects.create(
            nom=nom,
            prenom=prenom,
            sexe=sexe,
            profession=profession,
            date_naissance=date_naissance,
        )

        messages.success(request, 'Votre Participation est enregistrée avec succès')
        return redirect('blog')
    