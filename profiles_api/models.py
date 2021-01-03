from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager): #This inherits from the BaseUserManager which is the default manager model that comes with Django
    """Manager for user profiles"""

    def create_user(self, email, name, password=None): #the default password is 'None', and because of the way the Dango password checking system works, a 'None' password won't work because it needs to be a hash, so basically until you set a password, you won't be able to authenticate a user.
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email) #this makes the second half of the email lowercase. This is to standardize the email. Some email providers have lowercase and uppercase for the first half.
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)
        user.is_superuser = True  #this item is automatically created by the PermissionsMixin
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'    #this overwrites the default username field which is normally called username, and we're replacing it with our email
    REQUIRED_FIELDS = ['name'] #The username field is required by default, so by setting username equal to email by default, it makes the email required. Since the username and email are already required, we manually add 'name' to the list of required fields.

    def get_full_name(self):
       """Retrieve full name of user"""
       return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of our user"""
        return self.email     