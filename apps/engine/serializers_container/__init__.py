from rest_framework import serializers
from apps.engine.schemas.reward import Reward
from apps.engine.schemas.staking import Staking
from apps.engine.schemas.activities import Activities
from apps.engine.schemas.user_staking import UserStaking
from apps.engine.schemas.transactions import Transaction
from apps.engine.schemas.user import User, SystemRoleEnum
from apps.engine.schemas.notifications import Notifications
from apps.engine.schemas.financial_transactions import FinancialTransactions
from rest_framework.permissions import BasePermission