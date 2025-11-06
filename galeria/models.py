from django.db import models
from datetime import datetime

# Create your models here.
class Fotografia(models.Model):
    CATEGORIAS = [
        ('NEBULOSA', 'Nebulosa'),
        ('GALÁXIA', 'Galáxia'),
        ('ESTRELA', 'Estrela'),
        ('PLANETA', 'Planeta')
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=CATEGORIAS, default='')
    descricao = models.TextField(null=False, blank=False)
    imagem = models.ImageField(upload_to='fotos/%Y/%m/%d', blank=True)
    publicacao = models.BooleanField(default=False)
    data_postagem = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return f'Fotografia: {self.nome} - {self.legenda}'