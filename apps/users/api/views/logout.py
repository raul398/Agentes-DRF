from datetime import datetime
from http.client import error
from django.contrib.sessions.models import Session
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token


class Logout(APIView):

    def post(self, request, *args, **kwargs):
        session_message = ''
        token_message = ''
        try:
            token = request.data['token']
            token = Token.objects.filter(key = token).first()

            if token:
                user = token.user

                all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
                if all_sessions.exists():
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get('_auth_user_id')):
                            session.delete()
                            session_message = 'Sesiones de usuario eliminadas'

                token.delete()

                token_message = 'Token eliminado'

                return Response({'session_message': session_message,'token_message': token_message}, status = status.HTTP_200_OK)
            return Response({'error': 'Error, no se ha encontrado unusuario con estas credenciales'}, status= status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error': 'No se ha encontrado token en la peticion'}, status = status.HTTP_409_CONFLICT)