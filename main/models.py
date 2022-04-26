from django.db import models

# Create your models here.
class Restaurant(models.Model):
    # fields for the restaurant table
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=10)
    description = models.TextField(max_length=5000)
    averageRating = models.FloatField(default=0)
    image = models.URLField(default=None, null= True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name