# Generated by Django 4.2.4 on 2023-08-11 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_tg_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tg_user_id',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='чат-ID в телеграмме'),
        ),
    ]
