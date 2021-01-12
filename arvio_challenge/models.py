from django.db import models
from datetime import date

# Create your models here.
class EnergyCertificate(models.Model):
    class Meta:
        db_table = 'certificates'

    property_id = models.CharField(max_length=30,unique=True)
    certificate_id = models.CharField(max_length=30)
    municipality = models.IntegerField()
    building = models.IntegerField()
    unit = models.IntegerField()
    heat_efficiency_lvl = models.CharField(max_length=4)
    date_stored = models.DateField(("Date"), default=date.today)





