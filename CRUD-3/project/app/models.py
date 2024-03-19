from django.db import models

# Create your models here.
class Book(models.Model):
  Bid = models.AutoField(primary_key=True)
  Bname = models.CharField(max_length=200)
  Bauthor = models.CharField(max_length=200)
  Bcontact = models.CharField(max_length=15)
  Bprice = models.CharField(max_length=8)
  Breleasedate = models.DateField()

  class Meta:
    db_table = 'book'

  def __str__(self):
    return self.Bname