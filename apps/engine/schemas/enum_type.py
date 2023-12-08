from apps.engine.schemas import Enum


class EnumType(str, Enum):
    @classmethod
    def choices(cls):
        return tuple((x.value, x.name) for x in cls)

    @classmethod
    def list(cls):
        return list(map(lambda x: x.value, cls))

    def __str__(self):
        return self.value


class StakingEnum(EnumType):
    PUBLISHED = "PUBLISHED"
    FINISHED = "FINISHED"


class SystemRoleEnum(EnumType):
    ADMIN = "ADMIN"
    USER = "USER"


class StatusTransactionEnum(EnumType):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    FAILED = "FAILED"


class StakingStatusEnum(EnumType):
    PUBLISHED = "PUBLISHED"
    FINISHED = "FINISHED"


class UserStakingStatusEnum(EnumType):
    STAKED = "STAKED"
    DONE = "DONE"


class TypeTransactionEnum(EnumType):
    DEPOSIT = "DEPOSIT"
    WITHDRAW = "WITHDRAW"
