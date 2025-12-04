from django.urls import path
from .views import (
    HomeView,
    AutorListView, AutorCreateView, AutorUpdateView, AutorDeleteView,
    LibroListView, LibroCreateView, LibroUpdateView, LibroDeleteView,
    GeneroListView, GeneroCreateView, GeneroUpdateView, GeneroDeleteView,
    EditorListView, EditorCreateView, EditorUpdateView, EditorDeleteView,
    ContratoListView, ContratoCreateView, ContratoUpdateView, ContratoDeleteView,
    DistribuidorListView, DistribuidorCreateView, DistribuidorUpdateView, DistribuidorDeleteView,
    EnvioListView, EnvioCreateView, EnvioUpdateView, EnvioDeleteView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    # Autores
    path('autores/', AutorListView.as_view(), name='autor_list'),
    path('autores/nuevo/', AutorCreateView.as_view(), name='autor_create'),
    path('autores/editar/<int:pk>/', AutorUpdateView.as_view(), name='autor_update'),
    path('autores/borrar/<int:pk>/', AutorDeleteView.as_view(), name='autor_delete'),

    # Libros
    path('libros/', LibroListView.as_view(), name='libro_list'),
    path('libros/nuevo/', LibroCreateView.as_view(), name='libro_create'),
    path('libros/editar/<int:pk>/', LibroUpdateView.as_view(), name='libro_update'),
    path('libros/borrar/<int:pk>/', LibroDeleteView.as_view(), name='libro_delete'),

    # Generos
    path('generos/', GeneroListView.as_view(), name='genero_list'),
    path('generos/nuevo/', GeneroCreateView.as_view(), name='genero_create'),
    path('generos/editar/<int:pk>/', GeneroUpdateView.as_view(), name='genero_update'),
    path('generos/borrar/<int:pk>/', GeneroDeleteView.as_view(), name='genero_delete'),

    # Editores
    path('editores/', EditorListView.as_view(), name='editor_list'),
    path('editores/nuevo/', EditorCreateView.as_view(), name='editor_create'),
    path('editores/editar/<int:pk>/', EditorUpdateView.as_view(), name='editor_update'),
    path('editores/borrar/<int:pk>/', EditorDeleteView.as_view(), name='editor_delete'),

    # Contratos
    path('contratos/', ContratoListView.as_view(), name='contrato_list'),
    path('contratos/nuevo/', ContratoCreateView.as_view(), name='contrato_create'),
    path('contratos/editar/<int:pk>/', ContratoUpdateView.as_view(), name='contrato_update'),
    path('contratos/borrar/<int:pk>/', ContratoDeleteView.as_view(), name='contrato_delete'),

    # Distribuidores
    path('distribuidores/', DistribuidorListView.as_view(), name='distribuidor_list'),
    path('distribuidores/nuevo/', DistribuidorCreateView.as_view(), name='distribuidor_create'),
    path('distribuidores/editar/<int:pk>/', DistribuidorUpdateView.as_view(), name='distribuidor_update'),
    path('distribuidores/borrar/<int:pk>/', DistribuidorDeleteView.as_view(), name='distribuidor_delete'),

    # Envios
    path('envios/', EnvioListView.as_view(), name='envio_list'),
    path('envios/nuevo/', EnvioCreateView.as_view(), name='envio_create'),
    path('envios/editar/<int:pk>/', EnvioUpdateView.as_view(), name='envio_update'),
    path('envios/borrar/<int:pk>/', EnvioDeleteView.as_view(), name='envio_delete'),
]