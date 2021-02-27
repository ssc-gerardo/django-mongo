from django.db import models

from apps.decks.models import Deck

class Card(models.Model):
    pregunta = models.CharField(max_length=255)
    respuesta = models.TextField()

    deck = models.ForeignKey(
        Deck, 
        on_delete=models.CASCADE,
        #null=True,
        #blank=True
        )

    def __str__(self):
        return self.pregunta
