from django.db import models

# Create your models here.
class School(models.Model):
    Name = models.CharField(max_length=30)

    def panels(self):
        return Panel.objects.filter(School__pk=self.pk)

    def rooms(self):
        return Room.objects.filter(School__pk=self.pk)

    def closets(self):
        return Closet.objects.filter(School__pk=self.pk)

    def __str__(self):
        return self.Name



class Closet(models.Model):
    Name = models.CharField(max_length=30)
    School = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )


class Panel(models.Model):
    Name = models.CharField(max_length=30)
    Voltage = models.CharField(max_length=20, default='0')
    Location = models.CharField(max_length=30, default='')
    Panels = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    School = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    Closet = models.ForeignKey(
        Closet,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )


    def Rooms(self):
        return Room.objects.filter(Panel__pk=self.pk)

    def __str__(self):
        return self.Name

class Room(models.Model):
    Name = models.CharField(max_length=30)
    OldName = models.CharField(max_length=30, default='')
    Type = models.CharField(max_length=30, default='')
    School = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    Panels = models.ManyToManyField(Panel,blank=True,)

    def __str__(self):
        return self.Name


class Circuit(models.Model):
    Name = models.CharField(max_length=100)
    Number = models.IntegerField(default=0)
    Panel = models.ForeignKey(
        Panel,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    Rooms = models.ManyToManyField(Room, blank=True,)

    def __str__(self):
        out = str(self.Panel) + ', curcuit ' + str(self.Number) + ': '
        return out

