from django.db import models

class Event(models.Model):
          
    title = models.CharField(max_length=100)
    description = models.TextField(default='Please input the information for this event.')
    # Add more fields as needed