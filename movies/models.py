from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=50, null=False)
    
    GENRE_CHOICES = [
        ('M', 'Miedo'),
        ('AC', 'Accion'),
        ('TR', 'Triller'),
        ('R', 'Romance'),
        ('MU', 'Musical'),
        ('C', 'Comedia'),
        ('F', 'Filosofico'),
        ('NA', 'No Definida')    
    ]
    genre = models.CharField(max_length=2, choices=GENRE_CHOICES, default='NA')
    director = models.CharField(max_length=50, null=False)
    publication_date = models.DateField(null=False)
    synopsis = models.TextField(null=True)
    
    def __str__(self):
        return f"{self.name} - {self.director}"