from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)


from datetime import date

class Profile(models.Model):
    STAR_SIGN_CHOICES = [
        ('aries', 'Jäär'),
        ('taurus', 'Sõnn'),
        ('gemini', 'Kaksikud'),
        ('cancer', 'Vähk'),
        ('leo', 'Lõvi'),
        ('virgo', 'Neitsi'),
        ('libra', 'Kaalud'),
        ('scorpio', 'Skorpion'),
        ('sagittarius', 'Ambur'),
        ('capricorn', 'Kaljukits'),
        ('aquarius', 'Veevalaja'),
        ('pisces', 'Kalad'),
    ]

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    star_sign = models.CharField(max_length=20, choices=STAR_SIGN_CHOICES, blank=True)
    bio = models.TextField(blank=True, verbose_name="Bio")

    def calculate_age(self):
        if self.user.date_of_birth:
            today = date.today()
            born = self.user.date_of_birth
            age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
            return age
        return None

    def __str__(self):
        return f"{self.user.username} profiil"



class Gallery(models.Model):
    profile = models.ForeignKey('Profile', related_name='gallery', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='users/gallery_photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.profile.user.username} pilt"