
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
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from ..schemas.user import User
from ..serializers_container.activities import (
    Activities,
    ActivitiesSerializer,
    ActivitiesCreateSerializer
)
from ..serializers_container.user import (
    IsAdminUser,
    UserRegisterSerializer,
    UserLoginSerializer,
    UserProfileSerializer
)
from ..serializers_container.notifications import (
    Notifications,
    NotificationsSerializer,
    NotificationsCreateSerializer
)

from ..serializers_container.staking import (
    Staking,
    StakingSerializer
)

from ..serializers_container.user_staking import (
    UserStaking,
    UserStakingSerializer
)

from ..serializers_container.transaction import (
    Transaction,
    TransactionSerializer
)

from ..serializers_container.reward import (
    Reward,
    RewardSerializer
)

from ..serializers_container.finan_transac import (
    FinancialTransactions,
    FinancialTransactionsSerializer
)