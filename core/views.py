from django.shortcuts import render
from django.db.models import Q
from .models import Patrimonio
from .forms import PatrimonioForm

# Create your views here.
def lista_patrimonio(request):
    busca = request.GET.get('q')
    filtro_estado = request.GET.get('estado')

    patrimonios = Patrimonio.objects.all()

    if busca:
        patrimonios = patrimonios.filter(
            Q(nome__icontains=busca) | Q(numero_tombamento__icontains=busca)
        )

    if filtro_estado:
        patrimonios = patrimonios.filter(estado=filtro_estado)
    
    context = {
        'patrimonios': patrimonios,
        'busca_atual': busca,          # Para manter o texto no input
        'estado_atual': filtro_estado  # Para manter o select marcado
    }

    return render(request, 'core/lista.html', context)

def novo_patrimonio(request):
    form = PatrimonioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_patrimonio')
    return render(request, 'core/form.html', {'form': form})