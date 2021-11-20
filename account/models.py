from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Represents a user's profile
    """
    class Meta:
        verbose_name = 'نمایه کاربری'
        verbose_name_plural = 'نمایه کاربری'

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    # important fields that are stored in User model:
    #   first_name, last_name, email, date_joined
    point = models.IntegerField('امتیاز', default=0)
    city = models.CharField('شهر نماینده',max_length=50, null=True, blank=True)

    def add_point(self):
        self.point += 1
        self.save()

    def __str__(self):
        if self.user.get_full_name():
            return self.user.get_full_name()
        else:
            return self.user.username

