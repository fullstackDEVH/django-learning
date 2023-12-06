from apps.engine.schemas.enum_type import StakingEnum
from apps.engine.schemas import (
    models, uuid
)
from apps.engine.schemas.user import User


class Staking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=32,
        choices=StakingEnum.choices(),
        default=StakingEnum.PUBLISHED.value,
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
