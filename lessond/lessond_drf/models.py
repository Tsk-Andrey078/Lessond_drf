from django.db import models

# Create your models here.
class NewsModel(models.Model):
    id = models.AutoField(primary_key=True)
    add_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    text = models.TextField()


