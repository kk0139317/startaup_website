from django.db import models

# Create your models here.

class ContactForm(models.Model):
    name = models.CharField(max_length=25, null=True)
    email = models.CharField(max_length=25, null=True)
    subject = models.CharField(max_length=50, null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.email