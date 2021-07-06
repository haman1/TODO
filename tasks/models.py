from django.db import models

# Create your models here.


class Todo(models.Model):
    complete = models.BooleanField(default=False)
    task = models.CharField(max_length=20)

    def __str__(self):
        return self.task

