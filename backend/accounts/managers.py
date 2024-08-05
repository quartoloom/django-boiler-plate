from django.contrib.auth.models import BaseUserManager
from portal.choices import UserTypeChoices,GenderChoices

class MyUserManager(BaseUserManager):
    def create_user(self, phone, full_name, email, password=None, is_guest=False, is_active=True):
        if not phone:
            raise ValueError("Users must have a Phone number")

        user = self.model(
            phone=phone,
            email=email,
            full_name=full_name,
            is_guest=is_guest,
            is_active=is_active,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    
    def create_superuser(self, phone, email=None,full_name="Super Admin",gender=GenderChoices.MALE, password=None, **kwargs):
            user = self.create_user(
                phone=phone,
                full_name=full_name,
                email=email,
                password=password,
            )
            user.is_active = True
            user.is_admin = True
            user.gender =gender
            user.user_type = UserTypeChoices.ADMIN
            user.save(using=self._db)
            return user