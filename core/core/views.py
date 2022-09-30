from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from core.models import Venta, Catalogo
from django.core.paginator import Paginator

class HomeView(View):
    def get(self, request, *args, **kwargs):
        
        context={

        }
        return render(request, 'pages/index.html', context)


class CompraView(View):
    def get(self, request, *args, **kwargs):
        venta = Venta.objects.all()

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
               
        context={
          

        }
        return render(request, 'pages/venta.html', context)
