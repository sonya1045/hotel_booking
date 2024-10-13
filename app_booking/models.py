from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Room(models.Model):
    number = models.IntegerField()
    capacity = models.IntegerField()
    location = models.TextField()
    discription = models.TextField()

    def __str__(self):
        return f"Кімната № {self.number} на {self.capacity} людей"
    
    class Meta:
        verbose_name = "Room"
        ordering = ["number", "capacity"]

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="bookings")
    room = models.ForeignKey(Room, on_delete = models.CASCADE, related_name = "bookings")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.room}"



