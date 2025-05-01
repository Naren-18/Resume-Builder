from django.db import models

class Mydata(models.Model):
    RollNo=models.CharField(max_length=30)
    SGPA=models.CharField(max_length=30)
    CGPA=models.CharField(max_length=30)