from django.db import models

# Create your models here.


class student(models.Model):
    # stu_id = models.IntegerField()
    first_name = models.CharField( max_length=100)
    last_name = models.CharField( max_length=100)
    department = models.CharField(max_length =200,choices = 
                                  (
                                      ('IT','IT'),
                                      ('Non IT','Non IT'),
                                      ('Accounting','Accounting'),
                                      ('Finance','Finance'),
                                      ('Desiger','Desiger')
                                  ))
    datetime = models.DateTimeField(auto_now=True)
    Active = models.BooleanField(default = True)


