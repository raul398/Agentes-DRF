
from django.contrib.auth.models import User
from apps.base.api.views.tools import *

from apps.base.api.validations.authentication_mixins import Authentication
from apps.users.api.serializers.user_token_serializers import UserTokenSerializer

class TokenRefreshAPIView(Authentication, APIView):
    
    def get(self, request, *args, **kwars):
        '''
        Hereda de Authentication self.user
        '''
        try:
            user_token = Token.objects.get(
                user = self.user)

            user = UserTokenSerializer(self.user)

            return Response(
                {'token': user_token.key,
                'user': user.data
                },
                status = status.HTTP_200_OK
            )

        except:
            return Response({'error': 'Invalid credentials'}, status = status.HTTP_400_BAD_REQUEST)
