from django.db import models

class Contact(models.Model):
    full_name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    message = models.CharField(max_length=1000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Name: " + self.full_name + " | Email: " + self.email