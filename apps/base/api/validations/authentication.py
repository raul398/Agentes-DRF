from datetime import timedelta
from django.utils import timezone
from django.conf import settings
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
#from rest_framework.exceptions import AuthenticationFailed


# Este clase verifica el tiempo de vida del token.
class ExpiredTokenAuthentication(TokenAuthentication):

    def expired_in(self, token):
        time_elapsed = timezone.now() - token.created
        left_time = timedelta(seconds= settings.TOKEN_EXPIRED_AFTER_SECOND) - time_elapsed
        return left_time

    def is_token_expired(self, token):
        return self.expired_in(token) < timedelta(seconds = 0)

    def token_expire_handler(self, token):
        is_expired = self.is_token_expired(token)
        if is_expired:
            user = token.user
            token.delete()
            token = self.get_model().objects.create(user = user)
        return (is_expired, token)
    
    def authenticate_credentials(self, key):
        user, token, message, is_expired = None, None, None, False
        try:
            token = self.get_model().objects.select_related('user').get(key = key)
            user = token.user
            state = status.HTTP_202_ACCEPTED
            
            if not token.user.is_active:
                message = 'Usuario no activo o eliminado'
                state = status.HTTP_401_UNAUTHORIZED
            is_expired, token = self.token_expire_handler(token)

            if is_expired:
                message = 'Su token ha expirado'
                state = status.HTTP_401_UNAUTHORIZED
                user = token.user

        except self.get_model().DoesNotExist:
            # Si el token no existe retornara un invlid token
            message = 'Invalid token'
            state = status.HTTP_400_BAD_REQUEST
        
        return (user, token, message, is_expired, state)