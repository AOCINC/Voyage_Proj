from django.db import models
from django.core.validators import RegexValidator




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
    


class Europe_Packages(models.Model):
    '''it includes all Europe packages and falls under interanation packages '''
    Trip_Name           = models.CharField(max_length=255, blank=False)
    Days                = models.PositiveIntegerField()
    Nights              = models.PositiveIntegerField()
    Datailed_Itinerary  = models.TextField()
    Location_Image      = models.FileField(upload_to='media/Europe/HolidayPackage_Images/')
    Package             = models.CharField(max_length=59, choices = package_choice, default = '')
    uploaded_at         = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        self.Location_Image.delete()
        super().delete(*args, **kwargs)
    
        

class Middle_East_Packages(models.Model):
    '''it includes all Middle East packages and falls under interanation packages '''
    Trip_Name           = models.CharField(max_length=255, blank=False)
    Days                = models.PositiveIntegerField()
    Nights              = models.PositiveIntegerField()
    Datailed_Itinerary  = models.TextField()
    Location_Image      = models.FileField(upload_to='media/MiddleEast/HolidayPackage_Images/')
    Package             = models.CharField(max_length=59, choices = package_choice, default = '')
    uploaded_at         = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        self.Location_Image.delete()
        super().delete(*args, **kwargs)

    
class SouthEast_Asia_Packages(models.Model):
    '''it includes all SouthEast Asia packages and falls under interanation packages '''
    Trip_Name           = models.CharField(max_length=255, blank=False)
    Days                = models.PositiveIntegerField()
    Nights              = models.PositiveIntegerField()
    Datailed_Itinerary  = models.TextField()
    Location_Image      = models.FileField(upload_to='media/SouthEast_Asia/HolidayPackage_Images/')
    Package             = models.CharField(max_length=59, choices = package_choice, default = '')
    uploaded_at         = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        self.Location_Image.delete()
        super().delete(*args, **kwargs)

    
flight_classes = (
                  ('Economy','Economy'),
                  ('Business','Business'),
                  
                )
class Flight_Booking(models.Model):
    Name    = models.CharField(max_length=159,default='')
    Phone   = models.CharField(max_length=12,validators = [RegexValidator(r'^\d{1,12}$')], default = '')
    Email   = models.EmailField(max_length=159,default = '')
    From    = models.CharField(max_length=199)
    To      = models.CharField(max_length= 199)
    Date    = models.DateField()
    Till_Date   = models.DateField(blank = True,null=True)
    Class   = models.CharField(max_length=89, choices = flight_classes)
    Adults  = models.PositiveIntegerField(default = 0)
    Children = models.PositiveIntegerField(blank = True,null=True,default=0)


Hotel_Classes = (
                  ('Economy','Economy'),
                  ('3-Star','3-Star'),
                  ('4-Star','4-Star'),
                  ('5-Star','5-Star'),
                )


class Hotel_Booking(models.Model):
    Name        = models.CharField(max_length=159,default='')
    Phone       = models.CharField(max_length=12,validators = [RegexValidator(r'^\d{1,12}$')], default = '')
    Email       = models.EmailField(max_length=159)
    Destination = models.CharField(max_length=199)
    Check_In    = models.DateField()
    Check_Out   = models.DateField(blank = True,null=True)
    Class       = models.CharField(max_length=89, choices = Hotel_Classes)
    Adults      = models.PositiveIntegerField(default = 0)
    Children    = models.PositiveIntegerField(blank = True,null=True,default=0)
    Rooms       = models.PositiveIntegerField(default = 0)


months = (
          ('1','1-Month'),
          ('2','2-Months'),
          ('3','3-Months'),
    
         )

class Visa_Enquiry(models.Model):
    Full_Name   = models.CharField(max_length=159,default='')
    Phone       = models.CharField(max_length=12,validators = [RegexValidator(r'^\d{1,12}$')], default = '')
    Email       = models.EmailField(max_length=159)
    Country     = models.CharField(max_length = 159)
    Duration    = models.CharField(max_length= 129, choices = months)



Transport = (
            ('Train','Train'),
            ('Bus','Bus'),
            )



class Transports_Enquiry(models.Model):
    Full_Name   = models.CharField(max_length=159,default='')
    Phone       = models.CharField(max_length=12,validators = [RegexValidator(r'^\d{1,12}$')], default = '')
    Email       = models.EmailField(max_length=159)
    Destination = models.CharField(max_length=129,default = '')
    Jouryney_Date  = models.DateField()
    Return_Date = models.DateField()
    Journey_By  = models.CharField(max_length=129, choices = Transport)



    