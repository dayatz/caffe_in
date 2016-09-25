from django.db import models
from versatileimagefield.fields import VersatileImageField


class NameDescriptionMixin(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Cafe(NameDescriptionMixin):
    photo = VersatileImageField(upload_to='cafe/')

    # Contact
    phone = models.CharField(max_length=12)
    fb = models.CharField(max_length=30, null=True, blank=True)
    tw = models.CharField(max_length=30, null=True, blank=True)

    # Location
    address = models.TextField()
    lng = models.CharField(max_length=20)
    lat = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Cafe"
        verbose_name_plural = "Cafes"

    def __str__(self):
        return self.name


class Menu(NameDescriptionMixin):
    cafe = models.ForeignKey(Cafe, related_name='menus')
    photo = VersatileImageField(upload_to='menu/')
    price = models.FloatField()

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"

    def __str__(self):
        return "%s: %s" % (self.cafe.name, self.name)


class Gallery(models.Model):
    cafe = models.ForeignKey(Cafe)
    caption = models.CharField(max_length=50, null=True, blank=True)
    photo = VersatileImageField(upload_to='cafe/')

    def __str__(self):
        return self.cafe.name
