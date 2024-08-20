# importar_arquivos.py
import os
from django.core.management.base import BaseCommand
from compartilhar.models import Arquivo
from django.conf import settings

class Command(BaseCommand):
    help = 'Importa arquivos existentes no diretório para o banco de dados'

    def handle(self, *args, **kwargs):
        media_root = settings.MEDIA_ROOT
        arquivos_dir = os.path.join(media_root, 'arquivos')
        for filename in os.listdir(arquivos_dir):
            file_path = os.path.join(arquivos_dir, filename)
            if os.path.isfile(file_path):
                # Cria um registro no banco de dados
                arquivo, created = Arquivo.objects.get_or_create(
                    nome=filename,
                    defaults={'arquivo': file_path}
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Arquivo "{filename}" importado com sucesso.'))
                else:
                    self.stdout.write(self.style.WARNING(f'Arquivo "{filename}" já existe no banco de dados.'))
