from rest_framework import serializers
from .models import Difinition


class DifinitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Difinition
        fields = ('name', 'kana', 'difinition', 'note')