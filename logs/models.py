from django.db import models
import uuid

statuChoices = [
    ('error' , 'error'),
    ('arquivo negado', 'arquivo negado'),
    ('arquivo aceito', 'arquivo aceito')
]

# Create your models here.
class Log(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=255, choices=statuChoices)
    description = models.CharField(max_length=255)
    dtLog = models.DateTimeField(auto_now_add=True)