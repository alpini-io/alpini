from django.db import models

# Create your models here.

class Pagina (models.Model):
    titolo = models.CharField(max_length=60)
    permalink = models.CharField(max_length=12, unique=True)
    aggiornamento = models.DateTimeField('Ultimo Aggionrnamento')
    testo = models.TextField('Contenuto', blank=True)

    def __str__(self):
        return self.titolo