from django.db import models


class Employee(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="images")  # media file
    designation = models.CharField(max_length=100)
    email_address = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=12, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.f_name
