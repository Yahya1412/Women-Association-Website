from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from shop.models import Commande
from blog.models import Participant
from django.db.models import Count
from django.db.models.functions import ExtractMonth
from django.db.models import Sum


def login_user(request):
    if request.method == 'POST':
        
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('stats')
        else:
            messages.success(request, ("Données de connexion invalides"))
            return redirect('login')
    
    else:
        return render(request, 'shop/login.html', {})


from django.db.models import Sum
from django.db.models.functions import ExtractMonth

def home(request):
    # Get all commandes and participants
    donné = Commande.objects.all()
    part = Participant.objects.all()

    # Calculate the number of commandes per region
    trm = Commande.objects.filter(pays='Grand Tunis').count()
    rep = Commande.objects.filter(pays='Nord ouest').count()
    ann = Commande.objects.filter(pays='Nord-est').count()
    enc = Commande.objects.filter(pays='Région du Sahel').count()
    att = Commande.objects.filter(pays='Sud ouest').count()
    eur = Commande.objects.filter(pays='Sud-est').count()
    
    # Calculate the number of participants per gender
    hom = Participant.objects.filter(sexe='Homme').count()
    fem = Participant.objects.filter(sexe='Femme').count()

    # Calculate the total cost of commandes per region
    total_costs = Commande.objects.values('pays').annotate(total_cost=Sum('total')).order_by('pays')

    # Create a dictionary to map each region to its total cost
    region_total_cost = {item['pays']: item['total_cost'] for item in total_costs}

    region_list = ['Grand Tunis', 'Nord ouest', 'Nord-est', 'Région du Sahel', 'Sud ouest', 'Sud-est']
    nomb_region_list = [trm, rep, ann, enc, att, eur]
    sexe_list = ['Homme', 'Femme']
    nomb_sexe_list = [hom, fem]

    # Calculate the number of commandes per month
    commandes_per_month = Commande.objects.annotate(month=ExtractMonth('date_commande')).values('month').annotate(count=Count('id')).order_by('month')
    
    # Create lists for months and their corresponding counts
    months = []
    commandes_count = []
    for commande in commandes_per_month:
        months.append(commande['month'])
        commandes_count.append(commande['count'])

    context = {
        'donné': donné,
        'region_list': region_list,
        'nomb_region_list': nomb_region_list,
        'part': part,
        'sexe_list': sexe_list,
        'nomb_sexe_list': nomb_sexe_list,
        'months': months,
        'commandes_count': commandes_count,
        'region_total_cost': region_total_cost,
        'total_costs' : total_costs, # Add total costs to the context
    }
    
    return render(request, 'shop/stats.html', context)



def logout_user(request):
    logout(request)
    messages.success(request, ("Vous étes Déconnecté"))
    return redirect('login')

    

    