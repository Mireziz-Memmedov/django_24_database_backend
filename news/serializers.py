from rest_framework import serializers
from .models import NewsCore

class NewsCoreSerializer(serializers.ModelSerializer):
    model = NewsCore
    fields = ['id', 'title', 'description', 'image']