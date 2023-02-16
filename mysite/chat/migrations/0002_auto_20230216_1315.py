# Generated by Django 3.2.9 on 2023-02-16 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_usermodel_photo'),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='user.usermodel'),
        ),
        migrations.AlterField(
            model_name='room',
            name='current_users',
            field=models.ManyToManyField(blank=True, related_name='current_rooms', to='user.UserModel'),
        ),
        migrations.AlterField(
            model_name='room',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='user.usermodel'),
        ),
    ]