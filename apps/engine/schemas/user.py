from apps.engine.schemas import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager, models, uuid
)
from apps.engine.schemas.enum_type import SystemRoleEnum


class UserManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, username, password=None, system_role=SystemRoleEnum.USER.value):
        if not email:
            raise ValueError('Users must have an email')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, system_role=system_role)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email, username, password, system_role=SystemRoleEnum.SUPER_ADMIN.value)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    avatar = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    system_role = models.CharField(
        max_length=32,
        choices=SystemRoleEnum.choices(),
        default=SystemRoleEnum.USER.value,
    )
    fullname = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=16)
    birthday = models.DateField(auto_now_add=True)
    settings = models.JSONField(default=dict)
    verify_code = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return str(self.id)
