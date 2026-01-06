from django.shortcuts import render
from .models import Patrimonio
from .forms import PatrimonioForm

# Create your views here.
def lista_patrimonio(request):
    patrimonios = Patrimonio.objects.all()
    return render(request, 'core/lista.html', {'patrimonios': patrimonios})

def novo_patrimonio(request):
    form = PatrimonioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_patrimonio')
    return render(request, 'core/form.html', {'form': form})