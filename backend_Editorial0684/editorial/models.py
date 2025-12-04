from django.db import models

# Create your models here.
class AutorEditorial(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    biografia = models.TextField()
    email = models.CharField(max_length=100)
    sitio_web = models.CharField(max_length=255)
    fecha_fallecimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class GeneroLiterario(models.Model):
    nombre_genero = models.CharField(max_length=50)
    descripcion = models.TextField()
    es_ficcion = models.BooleanField()
    epoca_popular = models.CharField(max_length=50)
    publico_objetivo = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_genero


class Editor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    fecha_contratacion = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    especialidad_genero = models.CharField(max_length=100)
    departamento = models.CharField(max_length=50)
    dni = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class LibroEditorial(models.Model):
    titulo = models.CharField(max_length=255)
    autor_principal = models.ForeignKey(AutorEditorial, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13)
    fecha_publicacion = models.DateField()
    num_paginas = models.IntegerField()
    genero = models.ForeignKey(GeneroLiterario, on_delete=models.SET_NULL, null=True)
    precio_tapa = models.DecimalField(max_digits=10, decimal_places=2)
    stock_almacen = models.IntegerField()
    editor = models.ForeignKey(Editor, on_delete=models.SET_NULL, null=True)
    estado_publicacion = models.CharField(max_length=50)
    formato = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo


class ContratoAutor(models.Model):
    libro = models.ForeignKey(LibroEditorial, on_delete=models.CASCADE)
    autor_principal = models.ForeignKey(AutorEditorial, on_delete=models.CASCADE)
    fecha_firma = models.DateField()
    porcentaje_regalias = models.DecimalField(max_digits=5, decimal_places=2)
    monto_adelanto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_fin_contrato = models.DateField()
    clausulas_especiales = models.TextField()
    id_agente_literario = models.IntegerField()

    def __str__(self):
        return f"Contrato {self.id} - {self.autor_principal}"


class Distribuidor(models.Model):
    nombre_distribuidor = models.CharField(max_length=100)
    contacto_principal = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    direccion_almacen = models.CharField(max_length=255)
    pais_distribucion = models.CharField(max_length=50)
    tipo_distribucion = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_distribuidor


class EnvioLibros(models.Model):
    libro = models.ForeignKey(LibroEditorial, on_delete=models.CASCADE)
    distribuidor = models.ForeignKey(Distribuidor, on_delete=models.CASCADE)
    fecha_envio = models.DateTimeField()
    cantidad_enviada = models.IntegerField()
    costo_envio = models.DecimalField(max_digits=10, decimal_places=2)
    estado_envio = models.CharField(max_length=50)
    fecha_recepcion_esperada = models.DateField()
    numero_seguimiento = models.CharField(max_length=50)

    def __str__(self):
        return f"Envio {self.id} - {self.libro}"