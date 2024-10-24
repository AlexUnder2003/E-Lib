from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    published_date = models.DateField()
    file = models.FileField(upload_to='books/')

    def __str__(self):
        return self.title
