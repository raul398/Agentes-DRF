from rest_framework.renderers import JSONRenderer
from rest_framework.authentication import get_authorization_header
from rest_framework.response import Response
from rest_framework import status
from apps.base.api.validations.authentication import ExpiredTokenAuthentication

class Authentication(object):

    def get_user(self, request):
        ''' La maner acorrecta de enviar es Authorization: token js49ied83j47dhwoq9234dhd7ee73
            el metodo .split() divide el valor de Authorization en 
            [b'token', b'js49ied83j47dhwoq9234dhd7ee73']
        '''
        token = get_authorization_header(request).split()
        is_expired = None
        if token:
            # Se hace try por si no se envia el token por lo que no existira token[1]
            try:
                # .decode() decodifica la forma binaria del valor de token
                # b'js49ied83j47dhwoq9234dhd7ee73' --> 'js49ied83j47dhwoq9234dhd7ee73'
                token = token[1].decode()
            except:
                return (None, 'No se han enviado las credenciales', is_expired, status.HTTP_409_CONFLICT)
            expire_token = ExpiredTokenAuthentication()
            user, token, message, is_expired, state = expire_token.authenticate_credentials(token)
            return (user, message, is_expired, state)
        return (None, 'No se han enviado las credenciales', is_expired, status.HTTP_409_CONFLICT)

    def dispatch(self, request, *args, **kwargs):
        user, message, is_expired, state = self.get_user(request)
        if type(user) != str and message == None:
            return super().dispatch(request, *args, **kwargs)
        response = Response({'error': message, 'expired': is_expired}, status = state)
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = 'application/json'
        response.renderer_context = {}
        return response