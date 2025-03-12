from rest_framework.exceptions import APIException
from rest_framework import status


class AccountAlreadyExistsException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'an Account with this email already exists.'
    default_code = 'account_already_exists'
