from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Ruta

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context = None)

class HomeRutasView(LoginRequiredMixin, TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'rutas.html', {'rutas': Ruta.rutas.all() })

class DetalleRutaView(LoginRequiredMixin, TemplateView):
    def get(self, request, **kwargs):
        codigo = kwargs["codigo"]
        return render(request, 'ruta.html', {'ruta': Ruta.rutas.get(codigo=codigo)})

class RutaCreate(LoginRequiredMixin, CreateView):
    model = Ruta 
    template_name = 'ruta_form.html'
    fields = '__all__'

class RutaUpdate(LoginRequiredMixin, UpdateView):
    model = Ruta 
    template_name = 'ruta_form.html'
    fields = ['nombre', 'inicio', 'punto1', 'punto2', 'punto3', 'punto4', 'punto5', 'fin']

class RutaDelete(LoginRequiredMixin, DeleteView):
    model = Ruta 
    template_name = 'ruta_confirm_delete.html'
    success_url = reverse_lazy('rutas')
