from django.contrib.auth.models import AbstractUser
from django.db import models
from ..core.sql import TruncateTableMixin

class SignUpUser(AbstractUser):
    pass

    def __str__(self):
         return self.username


class Home(models.Model):
      class Meta:
            verbose_name = ('Home')
            verbose_name_plural = ('Home')

      background_image = models.ImageField(upload_to='home_images', blank=True)
      front_text = models.CharField(max_length=100, blank=True)
      middle_text = models.CharField(max_length=100, blank=True)
      last_text = models.CharField(max_length=100, blank=True)


class Biography(models.Model):
      class Meta:
           verbose_name_plural = ('Biography')

      name = models.CharField(max_length=30, blank=True)
      profile = models.CharField(max_length=100, blank=True)
      email = models.CharField(unique=True, max_length=40, blank=True)
      phone  = models.CharField(max_length=30, null=True, blank=True)
      image = models.ImageField(upload_to='bio_images', blank=True)

      def __str__(self):
          return self.name

class Skills(TruncateTableMixin, models.Model):
      class Meta:
          verbose_name_plural = ('Skills')
          ordering = ['-name']

      name = models.CharField(max_length=30, blank=True)
      percentage = models.PositiveIntegerField()

      def __str__(self):
          return self.name

class Services(TruncateTableMixin, models.Model):
      class Meta:
           verbose_name_plural  = ('Services')
           ordering = ['id']

      image = models.ImageField(upload_to='service_images', blank=True)
      service = models.CharField(max_length=30, blank=True)
      description = models.CharField(max_length=100, blank=True)

      def __str__(self):
          return self.service


class Portfolio(models.Model):
      class Meta:
            verbose_name_plural = ('Portfolio')
            ordering = ['id']

      CATEGORY_CHOICES = [
          ('app','App'),
          ('card','Card'),
          ('web', 'Web'),
      ]

      image = models.ImageField(upload_to='portfolio_images', blank=True)
      header_four = models.CharField(max_length=30, blank=True)
      italics = models.CharField(max_length=30, blank=True)
      category = models.CharField(max_length=30, blank=True, choices=CATEGORY_CHOICES)

      def __str__(self):
          return self.category


class Testimonial(models.Model):
    class Meta:
        verbose_name_plural = ('Testimonial')
        ordering = ['id']

    description = models.CharField(max_length=500, blank=True)
    image = models.ImageField(upload_to='Testimonial_images', blank=True)
    name = models.CharField(max_length=50, blank=True)
    title = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

class Contact(models.Model):
     class Meta:
         verbose_name_plural = ('Contact')
         ordering = ['id']

     name = models.CharField(max_length=50, blank=True)
     email = models.EmailField(max_length=254)
     subject = models.CharField(max_length=50)
     message = models.TextField(max_length=200, blank=True)

     def __str__(self):
         return self.name