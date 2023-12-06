from apps.engine.schemas import models, uuid
from apps.engine.schemas.enum_type import StatusTransactionEnum, TypeTransactionEnum
from apps.engine.schemas.user import User


class FinancialTransactions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=32,
        choices=StatusTransactionEnum.choices(),
        default=StatusTransactionEnum.PENDING.value,
    )
    type_transaction = models.CharField(
        max_length=32,
        choices=TypeTransactionEnum.choices(),
    )
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    tx_hash = models.CharField(max_length=256)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
