from django.core.management.base import BaseCommand
from core.models import Categoria, Localizacao, Patrimonio
import random
from datetime import date, timedelta

class Command(BaseCommand):
    help = 'Popula o banco de dados com dados fictícios para teste'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Limpando dados antigos...'))
        Patrimonio.objects.all().delete()
        Categoria.objects.all().delete()
        Localizacao.objects.all().delete()

        self.stdout.write('Criando categorias...')
        lista_cats = ['Informática', 'Mobiliário', 'Eletrônicos', 'Climatização', 'Veículos']
        cats_objs = [Categoria.objects.create(nome=c) for c in lista_cats]

        self.stdout.write('Criando localizações...')
        lista_locs = [
            ('Laboratório 01', 'Bloco C'), ('Sala dos Professores', 'Bloco A'),
            ('Almoxarifado', 'Térreo'), ('Recepção', 'Entrada'), ('Diretoria', 'Bloco A')
        ]
        locs_objs = [Localizacao.objects.create(sala=s, bloco=b) for s, b in lista_locs]

        self.stdout.write('Criando patrimônios...')
        itens_mock = [
            ('Notebook Dell Latitude 3420', 4500.00), ('Cadeira Gamer', 1200.00),
            ('Projetor Epson', 2800.00), ('Ar Condicionado 12000 BTUs', 1900.00),
            ('Mesa em L', 1200.00), ('Monitor 24pol', 900.00),
            ('Impressora Laser', 1500.00), ('Switch 24p', 1100.00),
            ('Estante de Aço', 450.00), ('Purificador', 600.00),
            ('Cafeteira Expresso', 350.00), ('Servidor Rack', 15000.00)
        ]
        estados = ['bom', 'bom', 'manutencao', 'inservivel']

        for i, (nome, valor) in enumerate(itens_mock):
            Patrimonio.objects.create(
                nome=nome,
                numero_tombamento=f"IFPI-{2026000 + i}",
                categoria=random.choice(cats_objs),
                localizacao=random.choice(locs_objs),
                data_aquisicao=date(2025, 1, 1) + timedelta(days=random.randint(0, 360)),
                valor=valor,
                estado=random.choice(estados),
                observacao="Dado gerado via seed."
            )

        self.stdout.write(self.style.SUCCESS('Concluído! Banco populado com sucesso.'))