from django.contrib.auth.models import UserManager as DefaultUserManager


class UserManager(DefaultUserManager):
    
    def _create_user(self, email:str, password:str, **extra_fields):
        if not email:
            raise ValueError('the email address must be provided')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email=email, password=password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('superusers must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)