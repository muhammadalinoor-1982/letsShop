# Generated by Django 4.2.3 on 2023-08-05 14:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('letsShop_Accounts_App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('phone', models.TextField(max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Address', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]