from django.db import models
from enum import Enum


class SystemRoleChoice(str, Enum):
    """system role of users"""

    ADMIN = "ADMIN"
    SUPER_ADMIN = "SUPER_ADMIN"
    USER = "USER"

    @classmethod
    def choices(cls):
        return tuple((x.value, x.name) for x in cls)

    @classmethod
    def list(cls):
        return list(map(lambda x: x.value, cls))

    def __str__(self):
        return self.value


class StatusTransactionChoice(str, Enum):
    """system role of users"""

    PENDING = "PENDING"
    APPROVED = "APPROVED"
    FAILED = "FAILED"

    @classmethod
    def choices(cls):
        return tuple((x.value, x.name) for x in cls)

    @classmethod
    def list(cls):
        return list(map(lambda x: x.value, cls))

    def __str__(self):
        return self.value


class TypeTransactionChoice(str, Enum):
    """system role of users"""

    DEPOSIT = "DEPOSIT"
    WITHDRAW = "WITHDRAW"

    @classmethod
    def choices(cls):
        return tuple((x.value, x.name) for x in cls)

    @classmethod
    def list(cls):
        return list(map(lambda x: x.value, cls))

    def __str__(self):
        return self.value


class StakingStatusChoice(str, Enum):
    """system role of users"""

    PUBLISHED = "PUBLISHED"
    FINISHED = "FINISHED"

    @classmethod
    def choices(cls):
        return tuple((x.value, x.name) for x in cls)

    @classmethod
    def list(cls):
        return list(map(lambda x: x.value, cls))

    def __str__(self):
        return self.value


class UserStakingStatusChoice(str, Enum):
    """system role of users"""

    STAKED = "STAKED"
    DONE = "DONE"

    @classmethod
    def choices(cls):
        return tuple((x.value, x.name) for x in cls)

    @classmethod
    def list(cls):
        return list(map(lambda x: x.value, cls))

    def __str__(self):
        return self.value


class User(models.Model):
    system_role = models.CharField(
        max_length=32,
        choices=SystemRoleChoice.choices(),
        default=SystemRoleChoice.USER.value,
    )
    username = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    hashed_password = models.CharField(max_length=256)
    fullname = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=16)
    birthday = models.DateField()

    avatar = models.ImageField(upload_to="User")
    is_active = models.BooleanField(default=False)
    settings = models.JSONField()
    verify_code = models.CharField(max_length=256)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Transaction(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=32,
        choices=StatusTransactionChoice.choices(),
        default=StatusTransactionChoice.PENDING.value,
    )
    from_address = models.CharField(max_length=256)
    to_address = models.CharField(max_length=256)
    tx_hash = models.CharField(max_length=256)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Activities(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.JSONField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class FinacialTransactions(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=32,
        choices=StatusTransactionChoice.choices(),
        default=StatusTransactionChoice.PENDING.value,
    )
    type_transaction = models.CharField(
        max_length=32,
        choices=TypeTransactionChoice.choices(),
    )
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    tx_hash = models.CharField(max_length=256)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Notifications(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Staking(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=32,
        choices=StakingStatusChoice.choices(),
        default=StakingStatusChoice.PUBLISHED.value,
    )
    contract_term = models.PositiveIntegerField()
    desc = models.TextField()
    max_out = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    asset = models.CharField(max_length=256)
    period = models.PositiveIntegerField()
    profit_rate = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserStaking(models.Model):
    staking_id = models.ForeignKey(Staking, on_delete=models.CASCADE)
    num_period = models.PositiveIntegerField()
    total_reward = models.PositiveIntegerField()
    status = models.CharField(
        max_length=32,
        choices=UserStakingStatusChoice.choices(),
        default=UserStakingStatusChoice.STAKED.value,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Reward(models.Model):
    user_staking_id = models.ForeignKey(UserStaking, on_delete=models.CASCADE)
    reward = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
