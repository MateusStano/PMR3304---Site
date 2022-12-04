from django.db import models
from django.conf import settings

class Album(models.Model):
    date = models.DateField(null=True)
    timeinit = models.TimeField(null=True)
    timefinal = models.TimeField(null=True)
    ESPECIALIDADES = [
        ('Angiologia',"Angiologia"),
        ('Dermatologia',"Dermatologia"),
        ('Endocrinologia',"Endocrinologia"),
        ('Gastroenterologia',"Gastroenterologia"),
        ('Ginecologia e obstetrícia',"Ginecologia e obstetrícia"),
        ('Oftalmologia',"Oftalmologia"),
        ('Ortopedia',"Ortopedia"),
        ('Otorrino',"Otorrino"),
        ('Pediatria',"Pediatria"),
        ('Psicologia',"Psicologia"),
        ('Psiquiatria',"Psiquiatria"),
        ('Neurologia',"Neurologia"),
        ('Nutricionista',"Nutricionista"),
        ('Urologia',"Urologia"),
        ('Outros', "Outros")
    ]
    especialidade = models.CharField(max_length=255, choices=ESPECIALIDADES, null="True")
    endereco = models.CharField(max_length=255,null=True    )
    info = models.CharField(blank=True,max_length=255000,default="")

    def __str__(self):
        return f'{self.date} - {self.time}'


class Review(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    MARCAR = [
        ('MarcaConsulta',"Marcar consulta"),
    ]
    especialidade = models.CharField(max_length=255, choices=MARCAR, null="True")
    text = models.CharField(max_length=255,null=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.text}" - {self.author.username}'


class List(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    albuns = models.ManyToManyField(Album)

    def __str__(self):
        return f'{self.name}'
