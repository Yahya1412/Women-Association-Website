from django.urls import path
from shop.views import home, index, detail, checkout, confirmation

urlpatterns = [
    path('', home, name='home'),
    path('index', index, name='products'),
    path('<int:myid>', detail, name="detail"),
    path('checkout', checkout, name="checkout"),
    path('confirmation', confirmation, name="confirmation" ),

]

