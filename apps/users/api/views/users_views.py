from apps.base.api.views.general_api_view import GeneralViewSet, GeneralPagination
from apps.users.api.serializers.user_serializers import UserSerializers


class UserViewPagination(GeneralPagination):
    page_size = 20

class UserViewSet(GeneralViewSet):
    pagination_class = UserViewPagination
    serializer_class = UserSerializers