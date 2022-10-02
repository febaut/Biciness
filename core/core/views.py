from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from core.models import Venta, Catalogo
from django.core.paginator import Paginator
from core.forms import FormVenta 
from django.core.files.storage import FileSystemStorage

class HomeView(View):
    def get(self, request, *args, **kwargs):
        
        context={

        }
        return render(request, 'pages/index.html', context)


class CompraView(View):
    def get(self, request, *args, **kwargs):
        venta = Catalogo.objects.all()

        venta_data = None

        if venta:
            paginator = Paginator(venta, 9)
            page_number = request.GET.get('page')
            venta_data  = paginator.get_page(page_number)
        
        context={
            'venta':venta_data
        }
        return render(request, 'pages/compra.html', context)

class VentaView(View):
    def get(self, request, *args, **kwargs):
        form = FormVenta()
               
        context={
            'form':form
          

        }
        return render(request, 'pages/venta.html', context)

    def post(self, request, *args, **kwargs):
        venta = Catalogo.objects.all()
        form = FormVenta(request.POST)

        if request.method == "POST":
            form = FormVenta(request.POST, request.FILES) 

            if form.is_valid():
                
                form.user = request.user
                nombre_p  = form.cleaned_data.get('nombre_producto')
                nombre_v  = form.cleaned_data.get('nombre_vendedor')
                marca     = form.cleaned_data.get('marca_cicla')
                precio    = form.cleaned_data.get('precio')
                ciudad    = form.cleaned_data.get('ciudad')
                contacto  = form.cleaned_data.get('contacto')
                imagen    = form.cleaned_data.get('imagen')

                p, created = Catalogo.objects.get_or_create(id_registro = form.user,
                                                            nombre_producto = nombre_p,
                                                            nombre_vendedor = nombre_v,
                                                            marca_cicla = marca,
                                                            precio = precio,
                                                            ciudad = ciudad,
                                                            contacto = contacto,
                                                            imagen = imagen
                                                            )
                p.save()
                return redirect('Compra')



        venta_data = None
        
        if venta:
            paginator = Paginator(venta, 9)
            page_number = request.GET.get('page')
            venta_data  = paginator.get_page(page_number)
        
        context={
            'venta':venta_data
        }
        
        return render(request, 'pages/venta.html', context)


class Productos(View):
    def get(self, request, *args, **kwargs):
        venta = Catalogo.objects.filter(id_registro=request.user)

        venta_data = None

        if venta:
            paginator = Paginator(venta, 9)
            page_number = request.GET.get('page')
            venta_data  = paginator.get_page(page_number)
        
        context={
            'venta':venta_data
        }
        return render(request, 'pages/productos.html', context)