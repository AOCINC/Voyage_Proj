from django.db import models




# Holiday package upload
class Holidays_Packages_Upload(models.Model):
    Trip_Name           = models.CharField(max_length=255, blank=False)
    Days                = models.PositiveIntegerField()
    Nights              = models.PositiveIntegerField()
    Datailed_Itinerary  = models.TextField()
    Location_Image      = models.FileField(upload_to='media/HolidayPackage_Images/')
    uploaded_at         = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        self.Location_Image.delete()
        super().delete(*args, **kwargs)
        
    
