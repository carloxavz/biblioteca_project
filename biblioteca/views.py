from django.shortcuts import render

from django.http import HttpResponse

from rest_framework import viewsets

from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Avg

from biblioteca.models import Autor, Libro, Resena
from biblioteca.serializers import AutorSerializer, LibroSerializer, ResenaSerializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    filterset_fields = ['autor', 'fecha_publicacion']
    ordering_fields = ['titulo', 'fecha_publicacion']

    def get_queryset(self):
        if self.request.query_params.get('reciente'):
            return Libro.objects.order_by('-fecha_publicacion')[:10]
        return Libro.objects.all()

    @action(detail=True, methods=['get'])
    def calificacion_promedio(self, request, pk=None):
        libro = self.get_object()
        calificacion_promedio = libro.resenas.aggregate(Avg('calificacion'))['calificacion__avg']
        return Response({'calificacion_promedio': calificacion_promedio})

class ResenaViewSet(viewsets.ModelViewSet):
    queryset = Resena.objects.all()
    serializer_class = ResenaSerializer

