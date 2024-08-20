from django.db import models

class Arquivo(models.Model):
    nome = models.CharField(max_length=255, blank=True)
    arquivo = models.FileField(upload_to='arquivos/')  # Os arquivos serão armazenados em 'media/arquivos/'

    def __str__(self):
        return self.nome

