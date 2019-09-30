from django.db import models


class spacexLaunchData(models.Model):
    mission_ID = models.CharField(primary_key=True, max_length=10,)
    flight_No = models.IntegerField(max_length=3)
    launch_Date = models.CharField(max_length=20)
    rocket_Manufacturer = models.CharField(max_length=25)

    # def __str__(self):
    #     return f"Mission ID: {mission_} - Flight No: {flight_No} - Launch Date: {launch_Date} - Manufacturer: {rocket_Manufacturer}"
