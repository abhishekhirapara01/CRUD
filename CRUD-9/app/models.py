from django.db import models

# Create your models here.
class Student(models.Model):
    sid = models.AutoField(primary_key=True)
    name = models.TextField()
    rollno = models.PositiveSmallIntegerField()
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'students'