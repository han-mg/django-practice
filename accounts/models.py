from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, AbstractUser, models
)

class User(AbstractBaseUser):
   email = models.EmailField(max_length=255, unique = True)
   nickname = models.CharField(max_length=255, blank=True, null=True)
   active = models.BooleanField(default=True) # 로그인 할 수 있나?(휴면계정이 아닌가?)
   staff = models.BooleanField(default=False) # superuser가 아닌 staff(김현준x 정택원o)
   admin = models.BooleanField(default=False) # superuser(김현준, 주영민)

   USERNAME_FIELD = 'email' # username을 email로 사용하겠다.
   REQUIRED_FIELDS = []
   def __str__(self):
        return self.email
    
