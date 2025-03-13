from rest_framework import serializers
import re


def validate_username(data):
    # regex pattern to check if username is an email
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(email_pattern, data['username']):
        return True
    raise serializers.ValidationError(code="invalid_username", detail="Username is not an email.")
