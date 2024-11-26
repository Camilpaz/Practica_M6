from django.forms import BaseModelForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django import forms

from .models import Vehiculo


    

# LoginRequiredMixin, PermissionRequiredMixin
class VehiculosView(LoginRequiredMixin, ListView):
    model = Vehiculo
    template_name = "vehiculos/vehiculos.html"
    context_object_name = 'vehiculos'
    login_url = reverse_lazy('login')  
    redirect_field_name = 'next'


    

class VehiculoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Vehiculo
    template_name = "vehiculos/create_vehiculo.html"
    fields = ['marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio']
    success_url = reverse_lazy('lista_vehiculos')
    permission_required = 'can.add_vehiculo_model'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(self.request, "Usted no tiene el nivel de acceso para acceder a la vista.")
            return redirect("lista_vehiculos")
        
        else:
            messages.info(self.request, "Primero debe iniciar sesión para continuar.")
            return redirect("login")
        
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['modelo'].widget = forms.TextInput(attrs={'class': 'form-control'})
        form.fields['serial_carroceria'].widget = forms.TextInput(attrs={'class': 'form-control'})
        form.fields['serial_motor'].widget = forms.TextInput(attrs={'class': 'form-control'})
        form.fields['precio'].widget = forms.TextInput(attrs={'class': 'form-control'})
        return form
    