from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers

__all__ = [
    'EmailSerializer',
    'PasswordTokenSerializer',
    'TokenSerializer',
]


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()


class PasswordTokenSerializer(serializers.Serializer):
    password = serializers.CharField(label=_("Password"), style={'input_type': 'password'})

    confirmed_password = serializers.CharField(
        style={"input_type": "password"}, write_only=True, label="Confirm password")
    token = serializers.CharField()

    def validate(self, data):
        """
        Check if passwords matched.
        """
        if data['password'] != data['confirmed_password']:
            raise serializers.ValidationError("passwords does not match")
        return data

class TokenSerializer(serializers.Serializer):
    token = serializers.CharField()
