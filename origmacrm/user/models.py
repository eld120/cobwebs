from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


# Create your models here.
class User(AbstractUser):
    #: First and last name do not cover name patterns around the globe
    name = models.CharField("Name of User", blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("user:detail", kwargs={"username": self.username})
