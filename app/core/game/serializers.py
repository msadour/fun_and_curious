from rest_framework import serializers

from app.core.game.models import Game, Question


class QuestionSerializer(serializers.ModelSerializer):

    label = serializers.CharField()

    class Meta:
        model = Question
        fields = "__all__"


class GameSerializer(serializers.ModelSerializer):

    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    author = serializers.CharField(source="author.username", read_only=True)

    class Meta:
        model = Game
        fields = "__all__"
