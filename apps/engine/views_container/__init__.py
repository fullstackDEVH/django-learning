
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.generics import (
    GenericAPIView,
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from ..schemas.user import User
from ..serializers_container.activities import (
    Activities,
    ActivitiesSerializer
)
from ..serializers_container.user import (
    UserRegisterSerializer,
    UserLoginSerializer,
    UserProfileSerializer,
    IsAdminUser
)
