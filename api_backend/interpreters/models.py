from django.db import models

# Create your models here.


class Interpreter(models.Model):
    name = models.CharField(max_length=200)

    # TODO tambah attributes lainnya

    def __str__(self):
        """A string representation of the model."""
        return self.name
