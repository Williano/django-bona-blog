# Core Django imports.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile-pic-default.jpg',
                              upload_to='profile_pics')
    banner_image = models.ImageField(default='slider-1.jpg',
                                     upload_to='banner')
    job_title = models.CharField(max_length=100)
    bio = models.CharField(max_length=100,
                           help_text="Short Bio (eg. I love cats and games)")

    address = models.CharField(max_length=100,
                               help_text="Enter Your Address"
                               )

    city = models.CharField(
                            max_length=100, help_text="Enter Your City"
                            )

    country = models.CharField(max_length=100,
                               help_text="Enter Your Country"
                               )

    zip_code = models.CharField(max_length=100,
                                help_text="Enter Your Zip Code"
                                )

    twitter_url = models.CharField(max_length=250, default="#",
                                   blank=True, null=True,
                                   help_text=
                                   "Enter # if you don't have an account")
    instagram_url = models.CharField(max_length=250, default="#",
                                     blank=True, null=True,
                                     help_text=
                                     "Enter # if you don't have an account")
    facebook_url = models.CharField(max_length=250, default="#",
                                    blank=True, null=True,
                                    help_text=
                                    "Enter # if you don't have an account")
    github_url = models.CharField(max_length=250, default="#",
                                  blank=True, null=True,
                                  help_text=
                                  "Enter # if you don't have an account")

    email_confirmed = models.BooleanField(default=False)

    created_on = models.DateTimeField(default=timezone.now)

    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
