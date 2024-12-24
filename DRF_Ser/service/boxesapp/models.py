from django.db import models


class Abstract(models.Model):
    name = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Box(Abstract):
    damaged = models.BooleanField(
        default=False
    )
    height = models.SmallIntegerField()
    width = models.SmallIntegerField()

    class Meta:
        ordering = ['pk']


class Item(Abstract):
    box = models.ForeignKey(
        to=Box,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='item'
    )
    value = models.SmallIntegerField()

    class Meta:
        ordering = ['pk']
