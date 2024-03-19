from django.db import models

# Create your models here.
class Movie(models.Model):
  Mid = models.AutoField(primary_key=True)
  Mname =  models.CharField( max_length=20, null=False)
  Mdirector = models.CharField(max_length=20)
  Mreleased_date = models.DateField()

  def __str__(self) :
    return self.Mname
  
  class Meta:
    db_table = 'movie'