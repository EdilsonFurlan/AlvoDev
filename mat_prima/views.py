from django.shortcuts import render,redirect
from .models import CategMatPrima,MatPrima

def inicio(request):
    categ=CategMatPrima.objects.all()
    return render(request,'mat_prima.html',{'categ':categ})

def list_categ(request):

    categ=CategMatPrima.objects.all()
    return render(request,'list_categ.html',{'categ':categ})

def mat_prima(request):
    categ_matprima=CategMatPrima.objects.all()
   # categ=CategMatPrima.objects.get(id=pk)
    categ=CategMatPrima.objects.all()
    matpri=MatPrima.objects.all
    return render(request,'mat_prima.html',{'categ':categ,'matpri':matpri,'categ_matprima':categ_matprima})

def cadastrar_matprima(request):
    nome=request.POST.get('nome')
    categoria=request.POST.get('tags')
    print(categoria)
    matprima=MatPrima(
        nome=nome,
        categoria_id = categoria
    )

    matprima.save()
    print(categoria)
    return redirect('mat_prima_url')
   
def cadastrar_categoria(request):

    nome=request.POST.get('nome')
    preco_unit=request.POST.get('preco_unit')
    unidade=request.POST.get('unidade')

    categoria=CategMatPrima(
        nome=nome,
        preco_unit=preco_unit,
        unidade=unidade
    )

    categoria.save()

    return redirect('mat_prima_url')

def inicio(request):
    return render(request,'index.html')