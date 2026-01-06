from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Localizacao(models.Model):
    sala = models.CharField(max_length=100)
    bloco = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.sala} - {self.bloco}"

class Patrimonio(models.Model):
    ESTADO_CHOICES = [
        ('bom', 'Bom Estado'),
        ('manutencao', 'Em Manutenção'),
        ('inservivel', 'Inservível'),
    ]

    nome = models.CharField(max_length=200)
    numero_tombamento = models.CharField(max_length=50, unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    localizacao = models.ForeignKey(Localizacao, on_delete=models.SET_NULL, null=True)
    data_aquisicao = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='bom')
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.numero_tombamento} - {self.nome}"