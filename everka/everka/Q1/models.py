from django.db import models

# Create your models here.
class Vehicule(models.Model):
    plate = models.CharField(max_length=300)
    created_time = models.DateTimeField(('created time'), auto_now_add=True)
    last_modified = models.DateTimeField(('last modified'), auto_now=True)

    class Meta:
        ordering = ['-created_time', '-last_modified']

    @property
    def get_related_navigation_records(self):
        return self.related_nav_rec.all()

    def __str__(self):
        return self.plate



class NavigationRecord(models.Model):
    vehicule = models.ForeignKey(Vehicule,related_name='related_nav_rec',on_delete=models.CASCADE)
    last_modified = models.DateTimeField(('last modified'), auto_now=True)
    created_time = models.DateTimeField(('created time'), auto_now_add=True)
    datetime = models.DateTimeField(('date time'))
    latitude = models.FloatField()
    longitude = models.FloatField()
    class Meta:
        ordering = ['-created_time', '-last_modified']

    def __str__(self):
        return self.vehicule.plate
