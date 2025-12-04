from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from .models import (
    AutorEditorial, GeneroLiterario, Editor, 
    LibroEditorial, ContratoAutor, Distribuidor, EnvioLibros
)

# --- HOME ---
class HomeView(TemplateView):
    template_name = "editorial/home.html"

# --- 1. AUTORES ---
class AutorListView(ListView):
    model = AutorEditorial
    # Django busca automáticamente: editorial/autoreditorial_list.html
    
class AutorCreateView(CreateView):
    model = AutorEditorial
    fields = '__all__'
    success_url = reverse_lazy('autor_list')
    # Django busca automáticamente: editorial/autoreditorial_form.html

class AutorUpdateView(UpdateView):
    model = AutorEditorial
    fields = '__all__'
    success_url = reverse_lazy('autor_list')

class AutorDeleteView(DeleteView):
    model = AutorEditorial
    success_url = reverse_lazy('autor_list')
    # Django busca automáticamente: editorial/autoreditorial_confirm_delete.html


# --- 2. GÉNEROS LITERARIOS ---
class GeneroListView(ListView):
    model = GeneroLiterario

class GeneroCreateView(CreateView):
    model = GeneroLiterario
    fields = '__all__'
    success_url = reverse_lazy('genero_list')

class GeneroUpdateView(UpdateView):
    model = GeneroLiterario
    fields = '__all__'
    success_url = reverse_lazy('genero_list')

class GeneroDeleteView(DeleteView):
    model = GeneroLiterario
    success_url = reverse_lazy('genero_list')


# --- 3. EDITORES ---
class EditorListView(ListView):
    model = Editor

class EditorCreateView(CreateView):
    model = Editor
    fields = '__all__'
    success_url = reverse_lazy('editor_list')

class EditorUpdateView(UpdateView):
    model = Editor
    fields = '__all__'
    success_url = reverse_lazy('editor_list')

class EditorDeleteView(DeleteView):
    model = Editor
    success_url = reverse_lazy('editor_list')


# --- 4. LIBROS ---
class LibroListView(ListView):
    model = LibroEditorial

class LibroCreateView(CreateView):
    model = LibroEditorial
    fields = '__all__'
    success_url = reverse_lazy('libro_list')

class LibroUpdateView(UpdateView):
    model = LibroEditorial
    fields = '__all__'
    success_url = reverse_lazy('libro_list')

class LibroDeleteView(DeleteView):
    model = LibroEditorial
    success_url = reverse_lazy('libro_list')


# --- 5. CONTRATOS ---
class ContratoListView(ListView):
    model = ContratoAutor

class ContratoCreateView(CreateView):
    model = ContratoAutor
    fields = '__all__'
    success_url = reverse_lazy('contrato_list')

class ContratoUpdateView(UpdateView):
    model = ContratoAutor
    fields = '__all__'
    success_url = reverse_lazy('contrato_list')

class ContratoDeleteView(DeleteView):
    model = ContratoAutor
    success_url = reverse_lazy('contrato_list')


# --- 6. DISTRIBUIDORES ---
class DistribuidorListView(ListView):
    model = Distribuidor

class DistribuidorCreateView(CreateView):
    model = Distribuidor
    fields = '__all__'
    success_url = reverse_lazy('distribuidor_list')

class DistribuidorUpdateView(UpdateView):
    model = Distribuidor
    fields = '__all__'
    success_url = reverse_lazy('distribuidor_list')

class DistribuidorDeleteView(DeleteView):
    model = Distribuidor
    success_url = reverse_lazy('distribuidor_list')


# --- 7. ENVÍOS ---
class EnvioListView(ListView):
    model = EnvioLibros

class EnvioCreateView(CreateView):
    model = EnvioLibros
    fields = '__all__'
    success_url = reverse_lazy('envio_list')

class EnvioUpdateView(UpdateView):
    model = EnvioLibros
    fields = '__all__'
    success_url = reverse_lazy('envio_list')

class EnvioDeleteView(DeleteView):
    model = EnvioLibros
    success_url = reverse_lazy('envio_list')