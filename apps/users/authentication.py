from datetime import timedelta
from django.utils import timezone
from django.conf import settings
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed


class ExpiredTokenAuthentication(TokenAuthentication):

    def expired_in(self, token):
        time_elapsed = timezone.now() - token.created
        left_time = timedelta(seconds= settings.TOKEN_EXPIRED_AFTER_SECOND) - time_elapsed
        return left_time

    def is_token_expired(self, token):
        return self.expired_in(token) < timedelta(second = 0)

    def token_expire_handler(self, token):
        is_expired = self.is_token_expired(token)
        if is_expired:
            print('TOKEN EXPIRADO')
        return is_expired
    
    def authenticate_credentials(self, key):
        try:
            token = self.get_model().objects.select_related('user').get(key = key)
        except self.get_model().DoesNotExist:
            raise AuthenticationFailed('Invalid token')

        if not token.user.is_active():
            raise AuthenticationFailed('Usuario no activo o eliminado')

        is_expired = self.token_expire_handler(token)

        if is_expired:
            raise AuthenticationFailed('Su token ha expirado')
        return (token.user, token)