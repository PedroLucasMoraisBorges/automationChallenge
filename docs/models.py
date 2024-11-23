from django.db import models
import uuid

# Create your models here.
class Docs(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    docName = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    url = models.CharField(max_length=255, null=True)
    dtRegister = models.DateTimeField()
    accepted = models.BooleanField(default=False)
    score = models.FloatField(default=0.0)
    isDeleted = models.BooleanField(default=False)

    def __str__(self):
        return self.docName