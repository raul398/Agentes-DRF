'''from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken'''

from apps.base.api.views.tools import *

from apps.users.api.serializers.user_token_serializers import UserTokenSerializer



class TokenRefreshAPIView(APIView):
    
    def get(self, request, *args, **kwars):
        username = request.GET.get('username')
        try:
            user_token = Token.objects.get(
                user = UserTokenSerializer().Meta.model.objects.filter(
                    username = username
                    ).first()
            )

            return Response(
                {'token': user_token.key},
                status = status.HTTP_200_OK
            )

        except:
            return Response({'error': 'Invalid credentials'}, status = status.HTTP_400_BAD_REQUEST)


class Login(ObtainAuthToken):

    def post(self, request, *args, **kwars):
        login_serializer = self.serializer_class(data = request.data, context = {'request': request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.is_active:
                # Se crean dos instacias
                # token --> contiene una clave token
                # created --> contien un valor booleano 
                # si se creo recientemente --> creates = True
                # si ya existia --> created = False
                token, created = Token.objects.get_or_create(user = user)
                user_serializer = UserTokenSerializer(user)
                if created:
                     return Response({
                    'token': token.key,
                    'user': user_serializer.data,
                    'message': 'User created succesfully'
                    }
                    , status= status.HTTP_201_CREATED)

                else:
                    '''
                    NOTA: Este codigo genera una sesion nueva y cierra las sesiones que esten iniciadas con el mismo id
                        si no hay sesiones en ejecucion y se creo un token lo elimina y crea uno nuevo

                    all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
                    if all_sessions.exists():
                        for session in all_sessions:
                            session_data = session.get_decoded()
                            if user.id == int(session_data.get('_auth_user_id')):
                                session.delete()
                    token.delete()
                    token = Token.objects.create(user = user)'''

                    # Este script impide que se inicie con un usuario que ya se encuentra en sesion y elimina el token que se creo.
                    token.delete()
                    return Response({'error': 'El usuario ingresado ya se encuentra en sesion'}, status = status.HTTP_409_CONFLICT)
               
            else:
                return Response({'error': 'Este usuario no puede iniciar session'}, status = status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'Usuario o contraseña incorrectos'}, status.HTTP_400_BAD_REQUEST)