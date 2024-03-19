from django.db import models

# Create your models here.
class Inventory(models.Model):
  Iid  = models.CharField(primary_key=True,max_length=10)
  Iname = models.CharField(max_length=200)
  Iprice = models.DecimalField(max_digits=10, decimal_places=2)
  Iquantity = models.PositiveIntegerField()

  class Meta:
    db_table = 'inventory'

  def __str__(self):
    return self.Iname
