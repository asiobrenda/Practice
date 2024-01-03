from django.db import models

class Tab(models.Model):

    class Meta:
        ordering = ['id']

    city_name = models.CharField(max_length=30, null=True)
    title = models.CharField(max_length=30, null=True)
    description = models.CharField(max_length=50, null=True)
    color = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.city_name