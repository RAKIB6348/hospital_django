from django.db import models


class Doctor(models.Model):
    image = models.ImageField(upload_to='doctor_images/', blank=True, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
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
    wage = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    allowance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    contract_start = models.DateField(null=True, blank=True)
    contract_end = models.DateField(null=True, blank=True)
    joining_date = models.DateField(null=True, blank=True)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def full_name(self):
        return ' '.join(part for part in (self.first_name, self.last_name) if part)

    def __str__(self):
        return self.full_name
