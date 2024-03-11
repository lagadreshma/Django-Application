from django.db import models

# Create your models here.

class CustomerRegistration(models.Model):
    customer_name = models.CharField(max_length=50)
    customer_email = models.EmailField(unique=True)
    customer_password = models.TextField(blank=False)
    customer_contact = models.CharField(max_length=10)  
    customer_address = models.TextField(blank=False)
    customer_profile_image = models.ImageField(upload_to="customer_profile_images")



    def __str__(self):
        return self.customer_name