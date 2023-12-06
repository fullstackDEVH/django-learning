from apps.engine.schemas import (
    models, uuid
)
from apps.engine.schemas.enum_type import UserStakingStatusEnum
from apps.engine.schemas.staking import Staking


class UserStaking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    staking_id = models.ForeignKey(Staking, on_delete=models.CASCADE)
    num_period = models.PositiveIntegerField()
    total_reward = models.PositiveIntegerField()
    status = models.CharField(
        max_length=32,
        choices=UserStakingStatusEnum.choices(),
        default=UserStakingStatusEnum.STAKED.value,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
