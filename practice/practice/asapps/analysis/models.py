from django.db import models

class Tabs(models.Model):
    class Meta:
        verbose_name_plural = 'Tabs'
        ordering = ['id']

    tab_name = models.CharField(max_length=200)
    saved_btn = models.JSONField(null=True)

    def __str__(self):
          return self.tab_name


