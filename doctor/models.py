from django.db import models


class Doctor(models.Model):
    image = models.ImageField(upload_to='doctor_images/', blank=True, null=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], default='male')
    specialization = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    present_address = models.CharField(max_length=255, blank=True)
    permanent_address = models.CharField(max_length=255, blank=True)
    education = models.CharField(max_length=255, blank=True)
    experience_years = models.PositiveIntegerField(default=0)
    fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    joining_date = models.DateField(null=True, blank=True)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
