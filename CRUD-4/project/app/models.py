from django.db import models

# Create your models here.
class Event(models.Model):
  Eid  = models.AutoField(primary_key=True)
  Ename = models.CharField(max_length=200)
  Elocation = models.CharField(max_length=50)
  Eprice = models.CharField(max_length=30)
  Econtact = models.CharField(max_length=15)

  class Meta:
    db_table = 'event'

  def __str__(self):
    return self.Ename