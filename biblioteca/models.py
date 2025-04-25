from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.core.exceptions import ValidationError
from django.db import models

def validar_nombre(valor):
    if not valor.strip():
        raise ValidationError('El nombre no puede estar vacío ni solo espacios.')        

class Autor(models.Model):
    nombre = models.CharField(max_length=100, validators=[validar_nombre])
    nacionalidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros')
    fecha_publicacion = models.DateField()    
    resumen = models.TextField(validators=[
        MinLengthValidator(30, message="El resumen debe tener al menos 30 caracteres.")
    ])

    def __str__(self):
        return self.titulo
    
class Resena(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='resenas')
    texto = models.TextField()
    calificacion = models.FloatField(validators=[
        MinValueValidator(0.0, message="El valor minimo es 1."),
        MaxValueValidator(5.0, message="El valor maximo es 5.")
    ])
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.libro.titulo} - {self.calificacion}/5"