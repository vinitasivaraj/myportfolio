from django.db import models

class Job(models.Model):
    Image=models.ImageField(upload_to='images/')
    Summary=models.CharField(max_length=300)


def __str__(self):
        return self.Summary