from django.contrib import admin
from .models import (
    AutorEditorial, GeneroLiterario, Editor, 
    LibroEditorial, ContratoAutor, Distribuidor, EnvioLibros
)

# Register your models here.
# Esto permite ver y buscar autores fácilmente
@admin.register(AutorEditorial)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'nacionalidad', 'email')
    search_fields = ('nombre', 'apellido')

# Esto organiza la vista de libros
@admin.register(LibroEditorial)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor_principal', 'isbn', 'stock_almacen', 'precio_tapa')
    list_filter = ('genero', 'estado_publicacion')
    search_fields = ('titulo', 'isbn')

# Registro simple para el resto de modelos
admin.site.register(GeneroLiterario)
admin.site.register(Editor)
admin.site.register(ContratoAutor)
admin.site.register(Distribuidor)
admin.site.register(EnvioLibros)