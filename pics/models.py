from django.db import models

# Create your models here.

class pic(models.Model):
    class Months(models.TextChoices):
        January = 'January'
        February = 'February'
        March = 'March'
        April = 'April'
        May = 'May'
        June = 'June'
        July = 'July'
        August = 'August'
        September = 'September'
        October = 'October'
        November = 'November'
        December = 'December'

    Image = models.ImageField(upload_to='images/')
    Description = models.TextField()
    Month = models.CharField(max_length=9, choices = Months.choices)
    Year = models.IntegerField(default = 2023, choices=((i,i) for i in range(2000, 2100)))
    Tag = models.CharField(max_length = 20)