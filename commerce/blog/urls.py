from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
       

urlpatterns = [
    path('',views.index,name="blog"), 
    path('ajouter_blog',views.ajouter_blog,name="ajouter_blog"),
    path('modifier_blog/<int:id>/', views.blog_edit, name='modifier_blog'),
    path('participer/', views.participer, name='participer'),
    path('blog_delete/<int:id>/', views.supprimer_blog, name='blog_delete'),

]

