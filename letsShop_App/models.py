from django.db import models
from django.contrib.auth.models import User

class Slider(models.Model):
    title       = models.CharField  (max_length=50)
    title1      = models.CharField  (max_length=50, null=True, blank=True)
    description = models.TextField  (null=True, blank=True)
    button_tag  = models.CharField  (max_length=50, null=True, blank=True)
    image       = models.ImageField (upload_to='slide_image/')

    def __str__(self):
        return str(self.title)

class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return str(self.title)

class SubCategory(models.Model):
    title   = models.CharField(max_length=50)
    category= models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return str(f'{self.title} >> {self.category}')

class Super_SubCategory(models.Model):
    title       = models.CharField(max_length=50)
    SubCategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)

class Size(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return str(self.title)

class Color(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return str(self.title)

class Condition(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return str(self.title)

class Product(models.Model):

    title               = models.CharField(max_length=50)
    category            = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory         = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    image               = models.ImageField(upload_to='product_image/')
    image1              = models.ImageField(upload_to='product_image/', null=True, blank=True)
    image2              = models.ImageField(upload_to='product_image/', null=True, blank=True)
    image3              = models.ImageField(upload_to='product_image/', null=True, blank=True)
    current_price       = models.DecimalField(max_digits=10, decimal_places=2)
    previous_price      = models.DecimalField(max_digits=10, decimal_places=2)
    description         = models.TextField(null=True, blank=True)
    short_description   = models.TextField()
    size                = models.ManyToManyField(Size)
    color               = models.ManyToManyField(Color)
    condition           = models.ManyToManyField(Condition)
    quantity            = models.PositiveIntegerField()
    trending_product    = models.BooleanField(default=False)
    featured_product    = models.BooleanField(default=False)
    top_seller          = models.BooleanField(default=False)
    deals_of_the_day    = models.BooleanField(default=False)
    wish_list           = models.BooleanField(default=False)
    created_at          = models.DateTimeField(auto_now=True)
    updated_at          = models.DateTimeField(auto_now=True)
    posted_by           = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)


