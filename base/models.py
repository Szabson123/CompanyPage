from django.db import models


class Question(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    text = models.TextField()
    
    def __str__(self) -> str:
        return f'{self.name} {self.last_name}, {self.email}'