from django.shortcuts import redirect, render
from .models import Product, Commande
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Commande
# Create your views here.
def home(request):
    
    return render(request, 'shop/home.html')
def index(request):
    product_object = Product.objects.all()
    item_name = request.GET.get('item-name')
    if item_name !='' and item_name is not None:
        product_object = Product.objects.filter(title__icontains=item_name)
    paginator = Paginator(product_object, 8)
    page = request.GET.get('page')
    product_object = paginator.get_page(page)
    return render(request, 'shop/index.html', {'product_object': product_object})
def detail(request, myid):
    product_object = Product.objects.get(id=myid)
    return render(request, 'shop/detail.html', {'product': product_object}) 
def checkout(request):
    if request.method == "POST":
        items = request.POST.get('items')
        total = request.POST.get('total')
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        address = request.POST.get('address')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        zipcode= request.POST.get('zipcode')
        com = Commande(items=items,total=total, nom=nom, email=email, address=address, ville=ville, pays=pays, zipcode=zipcode)
        com.save()
        return redirect('confirmation')
    return render(request, 'shop/checkout.html') 
# views.py


def confirmation(request):
    # Récupère la dernière commande
    commande = Commande.objects.latest('date_commande')
    items = commande.items.split(',')  # Supposons que les items soient séparés par des virgules
    total = commande.total
    nom = commande.nom
    email = commande.email
    address = commande.address
    ville = commande.ville
    pays = commande.pays
    zipcode = commande.zipcode
    date_commande = commande.date_commande

    context = {
        'items': items,
        'total': total,
        'nom': nom,
        'email': email,
        'address': address,
        'ville': ville,
        'pays': pays,
        'zipcode': zipcode,
        'date_commande': date_commande,
    }
    return render(request, 'shop/confirmation.html', context)



    

