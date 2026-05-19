from django.db import models

# Create your models here.

class movies (models.Model):
    Name = models.CharField(max_length=50, null= False)
    
    
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
    Genre = models.CharField(max_length=2, choices=GENRE_CHOICES, default='NA')
    Director = models,models.CharField(max_length=50, null=False)
    Publication_Date = models.DateField(null=False)
    Sinopsis = models.TextField(null=True)
    
    def __str__(self):
        return F"{self.Name}{self.Genre}{self.Director}"