from apps.engine.schemas import models, uuid
from ..utils.contant import SettingSystem

settings_system = SettingSystem()

class SystemInformation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    statistical = models.JSONField()
    tier = models.JSONField(default=settings_system.tiers)
    settings = models.JSONField(default=settings_system.settings)
    system_wallets = models.JSONField(default=settings_system.system_wallet)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
