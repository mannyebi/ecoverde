from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Blog_tag(models.Model):
    name = models.CharField(max_length=264)

    def __str__(self):
        return str(self.name)



class Property_type(models.Model):
    name = models.CharField(max_length=264)

    def __str__(self):
        return str(self.name)

class User(AbstractUser):
    image = models.ImageField(null=True, default='person_1.jpg')
    listings = models.ManyToManyField('Properties', related_name='listings', blank=True)


class Region(models.Model):
    country = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    
    def __str__(self):
        return str(f'{self.country} -- {self.city}')


class Properties(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(null=True, default='xperson_1.jpg.pagespeed.ic.P4pHl6glbj.jpg')
    video = models.TextField(null=True)
    tags = models.ForeignKey(Property_type, related_name='property_type', on_delete=models.SET_NULL, null=True, blank=True )
    Lot_Area = models.IntegerField()
    Floor_Area = models.IntegerField()
    Bed_Rooms = models.IntegerField()
    Bath_Rooms = models.IntegerField()
    Luggage = models.BooleanField()
    Garage = models.IntegerField()
    Year_Build = models.DateTimeField()
    Region = models.ForeignKey(Region, related_name='Region', on_delete=models.SET_NULL, null=True)
    host = models.ForeignKey(User, related_name='host', on_delete=models.CASCADE)
    status_choice = (
        ('rent', 'rent'),
        ('sale', 'sale') 
    )
    status = models.CharField(max_length=64, choices=status_choice, default='rent')
    price = models.IntegerField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)
    


class Areas(models.Model):
    property = models.ForeignKey(Properties, on_delete=models.CASCADE)
    area = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return str(self.area)


class Image(models.Model):
    image = models.ImageField(null=False)
    property = models.ForeignKey(Properties, related_name='properties', on_delete=models.CASCADE)
    area = models.ForeignKey(Areas, on_delete=models.CASCADE)

    def __str__(self):
        return str(f'{self.area} images')


class Panorama(models.Model):
    image_link = models.CharField(max_length=500)
    property = models.ForeignKey(Properties, related_name='info', on_delete=models.CASCADE)
    area = models.ForeignKey(Areas, on_delete=models.CASCADE)

    def __str__(self):
        return str(f'{self.area} panaromas')



class Blogs(models.Model):
    title = models.CharField(max_length=264)
    image = models.ImageField(null=False)
    body = models.TextField()
    #comments = models.foreignkey()
    auther = models.ForeignKey(User, related_name='auther', on_delete=models.SET_NULL, null=True)
    tags = models.ForeignKey(Blog_tag,related_name='topic', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(f'{self.title} by {self.auther}')


class Responses(models.Model):
    pass


class SavedProperties(models.Model):
    property = models.ForeignKey(Properties, on_delete=models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE)
    
    def __str__(self):
        return str(self.property)