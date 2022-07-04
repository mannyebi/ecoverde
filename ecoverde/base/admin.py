from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.User)
admin.site.register(models.Region)
admin.site.register(models.Properties)
admin.site.register(models.Image)
admin.site.register(models.Areas)
admin.site.register(models.Panorama)
admin.site.register(models.Blogs)
admin.site.register(models.Blog_tag)
admin.site.register(models.Property_type)
admin.site.register(models.SavedProperties)