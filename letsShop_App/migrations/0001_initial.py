# Generated by Django 4.2.3 on 2023-08-14 12:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('title1', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('button_tag', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.ImageField(upload_to='slide_image/')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='letsShop_App.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='product_image/')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='product_image/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='product_image/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='product_image/')),
                ('current_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('previous_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('short_description', models.TextField()),
                ('quantity', models.PositiveIntegerField()),
                ('trending_product', models.BooleanField(default=False)),
                ('featured_product', models.BooleanField(default=False)),
                ('top_seller', models.BooleanField(default=False)),
                ('deals_of_the_day', models.BooleanField(default=False)),
                ('wish_list', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='letsShop_App.category')),
                ('color', models.ManyToManyField(to='letsShop_App.color')),
                ('condition', models.ManyToManyField(to='letsShop_App.condition')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('size', models.ManyToManyField(to='letsShop_App.size')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='letsShop_App.subcategory')),
            ],
        ),
    ]
