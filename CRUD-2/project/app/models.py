from django.db import models

# Create your models here.
class Student(models.Model):
  Sname = models.CharField(max_length=10) 
  Sroll_num = models.PositiveSmallIntegerField(primary_key=True)
  Scourse = models.CharField(max_length = 20)
  Sstandard = models.PositiveIntegerField()
  def __str__(self):
    return self.Sname   
  class Meta:
    db_table = 'student'