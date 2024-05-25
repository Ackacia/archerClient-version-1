from django.core.exceptions import ValidationError
import pyotp
from auth2FA.models import UserTwoFactorAuthData


def user_two_factor_auth_data_create(*, user) -> UserTwoFactorAuthData:
    if hasattr(user, 'two_factor_auth_data'):
        raise ValidationError(
            'Ne peut pas avoir plus d’une donnée liée à 2FA.'
        )

    two_factor_auth_data = UserTwoFactorAuthData.objects.create(
        user=user,
        otp_secret=pyotp.random_base32()
    )

    return two_factor_auth_data


def user_two_factor_auth_data_get(*, user) -> UserTwoFactorAuthData:
    two_factor_auth_data = UserTwoFactorAuthData.objects.filter(user=user).first()
    return two_factor_auth_data
