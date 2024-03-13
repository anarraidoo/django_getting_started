from datetime import time

from django.db import models


# Adding a Room model
class Room(models.Model):
    name = models.CharField(max_length=50)
    room_number = models.IntegerField(default=1)
    floor = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.name}: room {self.room_number} on floor: {self.floor}"


# Adding a Meeting model
class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"
