from apps.engine.views_container import (
    User, Response, status, GenericAPIView, JSONParser, MultiPartParser, FormParser, IsAuthenticated, IsAdminUser,
    UserRegisterSerializer, UserLoginSerializer, UserProfileSerializer, LimitOffsetPagination
)


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
    serializer_class = UserProfileSerializer  # Specify the serializer class

    def get(self, request):
        """
        Create a new user.
        """
        serializer = UserProfileSerializer(request.user, many=False)
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
