# dacha_project/dacha_app/models.py

from django.db import models

class Dacha(models.Model):
    Dacha_image = models.ImageField(upload_to='images', null=True, blank=True)
    Dacha_name = models.CharField(max_length=255)
    Dacha_maydoni = models.FloatField()
    Dacha_nechtaxona = models.PositiveIntegerField()
    Dacha_sharoitlari = models.CharField(max_length=355)
    Dacha_address = models.CharField(max_length=255)
    Dacha_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.Dacha_name

class YangiModel(models.Model):
    # Yangi modelning maydonlari
    ...

    def __str__(self):
        # Qo'shilgan modelning nomi
        ...
