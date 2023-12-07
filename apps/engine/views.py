from rest_framework.generics import (
    GenericAPIView,
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from .schemas.user import User
from .schemas.activities import Activities
from rest_framework import permissions
from .serializers import (
    UserProfileSerializer,
    UserAllProfileSerializer,
    ActivitiesSerializer,
    UserLoginSerializer,
    UserRegisterSerializer,
    IsAdminUser,
)
from rest_framework.pagination import LimitOffsetPagination


class RegisterUserView(GenericAPIView):
    parser_classes = [JSONParser, MultiPartParser, FormParser]
    serializer_class = UserRegisterSerializer  # Specify the serializer class

    def post(self, request):
        """
        Create a new user.
        """
        # if email is already in use
        if User.objects.filter(email=request.data["email"]).exists():
            return Response(
                {"error": "Email already registered"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        else:
            serializer = UserLoginSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginUserView(GenericAPIView):
    parser_classes = [JSONParser, MultiPartParser, FormParser]
    serializer_class = UserLoginSerializer  # Specify the serializer class

    def post(self, request):
        """
        Create a new user.
        """
        # if email is already in use
        if User.objects.filter(email=request.data["email"]).exists():
            return Response(
                {"error": "Email already registered"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        else:
            serializer = UserLoginSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    parser_classes = [JSONParser, MultiPartParser, FormParser]
    serializer_class = UserAllProfileSerializer  # Specify the serializer class

    def get(self, request):
        """
        Create a new user.
        """
        serializer = UserAllProfileSerializer(request.user, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # update user profile image
    def put(self, request):
        user = User.objects.get(email=request.user.email)
        user.avatar = request.data["avatar"]
        user.save()
        return Response({"message": "Image updated"}, status=status.HTTP_200_OK)


class AllUsersView(GenericAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = UserProfileSerializer  # Specify the serializer class
    pagination_class = LimitOffsetPagination

    def get(self, request):
        users = User.objects.all()
        serializer = UserProfileSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ActivitiesListAPIView(ListAPIView):
    queryset = Activities.objects.all()
    serializer_class = ActivitiesSerializer
    permission_classes = [permissions.AllowAny]


class ActivitiesDetailAPIView(RetrieveAPIView):
    queryset = Activities.objects.all()
    serializer_class = ActivitiesSerializer
    permission_classes = [permissions.AllowAny]


class ActivitiesCreateAPIView(CreateAPIView):
    queryset = Activities.objects.all()
    serializer_class = ActivitiesSerializer
    permission_classes = [permissions.IsAuthenticated]

    # override the default method create
    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)
        return super().perform_create(serializer)


class ActivitiesUpdateAPIView(UpdateAPIView):
    queryset = Activities.objects.all()
    serializer_class = ActivitiesSerializer
    permission_classes = [permissions.IsAuthenticated]


class ActivitiesDeleteAPIView(DestroyAPIView):
    queryset = Activities.objects.all()
    serializer_class = ActivitiesSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserActivitiesAPIView(ListAPIView):
    serializer_class = ActivitiesSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = LimitOffsetPagination

    # override the default method create
    def get_queryset(self):
        # user_id = self.kwargs.get('user_id')
        queryset = Activities.objects.filter(user_id=self.request.user)
        return queryset
