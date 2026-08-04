from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)
    number_of_doctors = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
