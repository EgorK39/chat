from django.db import models
from django.contrib.auth.models import User


class UserModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    photo = models.ImageField(upload_to='images', null=True, blank=True, db_column='Фото', default='images/default2.jpg')
    about = models.TextField()

    def __str__(self):
        return f'{self.user}'
