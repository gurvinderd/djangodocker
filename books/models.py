from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200)
    read_on = models.DateTimeField()
    notes = models.TextField(default="", blank=True)

    def __str__(self):
    	return self.title