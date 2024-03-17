from rest_framework import serializers

from .models import Address


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ("id", "name", "address", "postalcode", "city", "country", "email")

    def validate(self, data):
        if 'country' in data and 'postalcode' in data:
            if data["country"] == "Utopia" and len(data["postalcode"]) != 7:
                raise serializers.ValidationError("The postal code for Utopia must be seven characters long.")
        return data
