from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=256)
    
    def __str__(self) -> str:
        return self.name
    
    
class Author(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    
    def get_full_name(self):
        return self.first_name + ' ' + self.last_name
    
    def __str__(self) -> str:
        return self.get_full_name()
    
    
    
class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    
    isbn = models.CharField(max_length=32)
    
    categories = models.ManyToManyField(Category, blank=True)
    pages_count = models.IntegerField()
    
    def __str__(self) -> str:
        return self.name
    
    
    