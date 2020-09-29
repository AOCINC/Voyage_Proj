from django.db import models




package_choice  = ( 
                    ('Domestic','Domestic'),
                    ('CentralAsia','Central-Asia'),
                    ('Europe','Europe'),
                    ('MiddleEast','Middle-East'), 
                    ('SouthEast_Asia','SouthEast-Asia'),                   
                    )

# Holiday package upload
class Holidays_Packages_Upload(models.Model):
    Trip_Name           = models.CharField(max_length=255, blank=False)
    Days                = models.PositiveIntegerField()
    Nights              = models.PositiveIntegerField()
    Datailed_Itinerary  = models.TextField()
    Location_Image      = models.FileField(upload_to='media/HolidayPackage_Images/')
    Package             = models.CharField(max_length=59, choices = package_choice, default = '')
    uploaded_at         = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        self.Location_Image.delete()
        super().delete(*args, **kwargs)



        
class Domestic_Holiday_Package(models.Model):
    ''' includes all the india packages '''
    Trip_Name           = models.CharField(max_length=255, blank=False)
    Days                = models.PositiveIntegerField()
    Nights              = models.PositiveIntegerField()
    Datailed_Itinerary  = models.TextField()
    Location_Image      = models.FileField(upload_to='media/Domestic/HolidayPackage_Images/')
    Package             = models.CharField(max_length=59, choices = package_choice, default = '')
    uploaded_at         = models.DateTimeField(auto_now_add=True)


    def delete(self, *args, **kwargs):
        self.Location_Image.delete()
        super().delete(*args, **kwargs)

class Central_Asia_Packages(models.Model):
    '''it includes all central asia packages and falls under interanation packages '''
    Trip_Name           = models.CharField(max_length=255, blank=False)
    Days                = models.PositiveIntegerField()
    Nights              = models.PositiveIntegerField()
    Datailed_Itinerary  = models.TextField()
    Location_Image      = models.FileField(upload_to='media/CentralAsia/HolidayPackage_Images/')
    Package             = models.CharField(max_length=59, choices = package_choice, default = '')
    uploaded_at         = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        self.Location_Image.delete()
        super().delete(*args, **kwargs)

        

    
