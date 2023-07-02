from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()
    photo = models.ImageField(upload_to='authors')

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    publication_date = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='books')

    def __str__(self):
        return self.title
