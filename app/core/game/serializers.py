from rest_framework import serializers

from app.core.game.models import Question


class QuestionSerializer(serializers.ModelSerializer):

    label = serializers.CharField()

    class Meta:
        model = Question
        fields = "__all__"
