from django.db import models

class TeamMember(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    role = models.BooleanField(default=False)
    email = models.EmailField()

