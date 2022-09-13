from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
   
class Book(models.Model):
    title=models.CharField(max_length=264)
    ratings=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])
    published=models.DateField(null=True,blank=True)
    
    def __str__(self):
        return self.title