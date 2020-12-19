from rest_framework import serializers
from fameza.models import User


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
        )

