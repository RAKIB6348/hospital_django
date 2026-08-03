from django.db import models


class Ward(models.Model):
    name = models.CharField(max_length=100)
    number_of_beds = models.PositiveIntegerField(default=0)
    available_beds = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Bed(models.Model):
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE, related_name='beds')
    bed_number = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=[
        ('available', 'Available'),
        ('occupied', 'Occupied'),
        ('maintenance', 'Maintenance'),
    ], default='available')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.bed_number} - {self.ward.name}'
