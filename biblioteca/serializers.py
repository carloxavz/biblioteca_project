from biblioteca.models import Autor, Libro, Resena
from rest_framework import serializers

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class ResenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resena
        fields = '__all__'

class LibroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Libro
        fields = '__all__'

        
    resenas_recientes = serializers.SerializerMethodField()
    autor_name = serializers.ReadOnlyField(source='autor.nombre')


    def get_resenas_recientes(self, obj):
        resenas = obj.resenas.all().order_by('-fecha')[:5]
        return ResenaSerializer(resenas, many=True).data

