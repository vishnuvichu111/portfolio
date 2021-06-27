from django.db import models





class Book(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Email = models.CharField(max_length=50,null=True,blank=True)
    Subject = models.CharField(max_length=50,null=True,blank=True)
    Message = models.CharField(max_length=500,null=True,blank=True)

    def __str__(self):
        return self.Name
