from datetime import datetime

from django.db import models

CATEGORIES_CHOICES = [
    ('dolorosos', 'Dolorosos'),
    ('gloriosos', 'Gloriosos'),
    ('gozosos', 'Gozosos'),
    ('luminosos', 'Luminosos'),
]

SEQUENCE_CHOICES = [
    ('1', 'Primeiro mistério'),
    ('2', 'Segundo mistério'),
    ('3', 'Terceiro mistério'),
    ('4', 'Quarto mistério'),
    ('5', 'Quinto mistério'),
]

class Mystery(models.Model):
    name = models.CharField(max_length=300, verbose_name='Mistério')
    category = models.CharField(choices=CATEGORIES_CHOICES, max_length=50, verbose_name='Categoria')
    sequence = models.CharField(choices=SEQUENCE_CHOICES, max_length=50, verbose_name='Ordem da sequência')
    image = models.ImageField(upload_to='photos/', verbose_name='Imagem')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de atualização')

    @staticmethod
    def get_mysteries_of_the_day():
        weekday = datetime.now().weekday()
        category = 'luminosos'

        if weekday in [1, 4]:
            category = 'dolorosos'
        elif weekday in [2, 6]:
            category = 'gloriosos'
        elif weekday in [0, 5]:
            category = 'gozosos'

        return Mystery.objects.filter(
            category=category).order_by('sequence')

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = 'mistério'
        verbose_name_plural = 'mistérios'
