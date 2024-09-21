from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    topics = models.ManyToManyField('Topic', related_name="categories")

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, related_name="category_topics", blank=True)
    slug = models.TextField()
    description = models.TextField()
    body = models.TextField()
    image1 = models.ImageField(upload_to='images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name
