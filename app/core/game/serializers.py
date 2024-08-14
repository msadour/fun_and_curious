from rest_framework import serializers

from app.core.game.models import Game
from app.core.user_profile.models import Profile


class GameSerializer(serializers.ModelSerializer):

    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    author = serializers.CharField(source="author.username", read_only=True)

    def create(self, validated_data):
        label: str = validated_data.get("label")
        author: Profile = validated_data.get("author")
        gender: str = validated_data.get("gender")
        only_soft: bool = validated_data.get("only_soft")

        new_game: Game = Game.objects.create(label=label)
        if author:
            new_game.author = author
        new_game.generate_content(gender=gender, only_soft=only_soft)
        new_game.save()

        return new_game

    class Meta:
        model = Game
        fields = "__all__"
