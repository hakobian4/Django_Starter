from lesson_8.models import GameModel, GamerModel, GamerLibraryModel
from rest_framework import serializers


class GameModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameModel
        fields = '__all__'


class GamerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GamerModel
        fields = ['nickname', 'email']