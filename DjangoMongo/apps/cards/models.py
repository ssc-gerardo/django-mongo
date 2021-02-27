from django.db import models

from apps.decks.models import Deck


class Card(models.Model):
    pregunta = models.CharField(max_length=255)
    respuesta = models.TextField()

    class TiposPreguntas(models.IntegerChoices):
        multiple_choice = 1
        fill_in_the_blank = 2
        true_or_flase = 3
        short_answer = 4
    tipo_pregunta = models.IntegerField(
        choices=TiposPreguntas.choices, default=4
    )

    deck = models.ForeignKey(
        Deck,
        on_delete=models.CASCADE,
        # null=True,
        # blank=True
        )

    def __str__(self):
        return self.pregunta
