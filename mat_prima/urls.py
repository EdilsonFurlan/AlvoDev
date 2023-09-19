from django.urls import path
from .import views

urlpatterns = [
    path('',views.inicio,name="mat_prima_url"),
    path('list_categ/',views.list_categ,name='list_categ_url'),
   # path('mat_prima/<int:pk>',views.mat_prima,name="mat_prima_url"),
    path('mat_prima',views.mat_prima,name="mat_prima_url"),
    path('cadastrar_matprima',views.cadastrar_matprima,name='cadastrar_matprima_url'),
    path('cadastrar_categoria',views.cadastrar_categoria,name='cadastrar_categoria_url'),
    path('',views.inicio,name='inicio_url')

]
