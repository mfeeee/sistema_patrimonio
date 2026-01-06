from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Patrimonio
from .forms import PatrimonioForm

# Create your views here.
@login_required
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

@login_required
def novo_patrimonio(request):
    form = PatrimonioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_patrimonio')
    return render(request, 'core/form.html', {'form': form})

@login_required
def editar_patrimonio(request, id):
    patrimonio = get_object_or_404(Patrimonio, pk=id)
    form = PatrimonioForm(request.POST or None, instance=patrimonio)
    
    if form.is_valid():
        form.save()
        return redirect('lista_patrimonio')
        
    return render(request, 'core/form.html', {'form': form})

@login_required
def deletar_patrimonio(request, id):
    patrimonio = get_object_or_404(Patrimonio, pk=id)
    
    if request.method == 'POST':
        patrimonio.delete()
        return redirect('lista_patrimonio')
        
    return render(request, 'core/confirmar_exclusao.html', {'patrimonio': patrimonio})