from django.db import models

# Create your models here.
class Event(models.Model):
    event_creator=models.CharField(max_length=40)
    event_password = models.CharField(max_length=40)
    banner = models.ImageField()
    event=models.CharField(max_length=40)
    venue = models.CharField(max_length=40)
    date=models.DateField()
    time=models.TimeField()
    contacts=models.IntegerField()
    cash=models.CharField(max_length=40)
    description=models.TextField(max_length=1000000)


    def __str__(self):
        return self.event


class Comment(models.Model):
    event_name=models.ForeignKey(Event,on_delete=models.CASCADE)
    user_name=models.CharField(max_length=40)
    opinions=models.TextField(max_length=1000000)

    def __str__(self):
        return self.user_name


