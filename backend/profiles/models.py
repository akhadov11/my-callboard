from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profile/', blank=True, null=True)
    second_email = models.EmailField("Confirm email")
    phone = models.CharField("Phone number", max_length=25)
    fname = models.CharField("First name", max_length=55)
    lname = models.CharField("Last name", max_length=55, blank=True, null=True)
    slug = models.SlugField("Url", max_length=50, default='')

    def __str__(self):
        return f"{self.fname} {self.lname}"

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     self.slug = f"{self.user_id}{self.fname}"

    # def get_absolute_url(self):
    #     return reverse("profile-detail", kwargs={"slug": self.user.username})

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
