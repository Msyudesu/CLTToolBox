from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Entry(models.Model):
    operator = models.ForeignKey(User, on_delete=CASCADE)
    prefix = models.CharField(max_length=8)
    count = models.IntegerField()
    hood = CharField(max_length=8)
    record_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.prefix}: {self.count} on {self.record_date} by {self.operator}"