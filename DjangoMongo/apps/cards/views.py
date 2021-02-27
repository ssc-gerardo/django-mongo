# from django.shortcuts import render
from rest_framework import serializers
from rest_framework import viewsets
from .models import Card
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'


class CardsViewSet(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    queryset = Card.objects.all()

    filter_backends = (
         filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ('tipo_pregunta',)
    search_fields = ('pregunta',)
    ordering = ('tipo_pregunta',)
