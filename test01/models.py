from django.db import models

# Create your models here.
class Difinition(models.Model):
    #id = models.CharField(primary_key=True, max_length=10)
    name = models.TextField(unique=True)
    kana = models.TextField()
    difinition = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
