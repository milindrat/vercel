from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class SalesOrder(models.Model):
    internalId = models.IntegerField()
    documentNumber = models.CharField(max_length=255)
    date = models.DateField()
    

    def __str__(self):
        return self.internalId
    

