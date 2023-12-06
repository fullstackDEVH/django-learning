from apps.engine.schemas import models, uuid
from apps.engine.schemas.user_staking import UserStaking


class Reward(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_staking_id = models.ForeignKey(UserStaking, on_delete=models.CASCADE)
    reward = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
