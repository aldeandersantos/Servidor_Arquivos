import os
from .models import Arquivo
from .forms import ArquivoForm
from django.http import HttpResponse, Http404
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect


def listar_arquivos(request):
    arquivos = Arquivo.objects.all()
    for arquivo in arquivos:
        arquivo.nome = os.path.basename(arquivo.arquivo.name)
    return render(request, 'listar_arquivos.html', {'arquivos': arquivos})

def baixar_arquivo(request, arquivo_id):
    try:
        arquivo = Arquivo.objects.get(pk=arquivo_id)
        caminho_arquivo = os.path.join(settings.MEDIA_ROOT, arquivo.arquivo.name)

        if os.path.exists(caminho_arquivo):
            with open(caminho_arquivo, 'rb') as f:
                response = HttpResponse(f.read(), content_type="application/octet-stream")
                response['Content-Disposition'] = f'attachment; filename="{os.path.basename(arquivo.arquivo.name)}"'
                return response
        else:
            raise Http404("Arquivo não encontrado.")
    except Arquivo.DoesNotExist:
        raise Http404("Arquivo não encontrado.")
    
def upload_arquivo(request):
    if request.method == 'POST':
        form = ArquivoForm(request.POST, request.FILES)
        if form.is_valid():
            arquivo = form.save()
            return redirect('listar_arquivos')
    else:
        form = ArquivoForm()
    return render(request, 'upload_arquivo.html', {'form': form})

def excluir_arquivo(request, arquivo_id):
    arquivo = get_object_or_404(Arquivo, pk=arquivo_id)
    if request.method == 'POST':
        if arquivo.arquivo:
            arquivo.arquivo.delete(save=False)
        arquivo.delete()
        return redirect('listar_arquivos')
    return render(request, 'confirmar_exclusao.html', {'arquivo': arquivo})