from django.db import models

# Create your models here.
class Covid(models.Model):
    name = models.CharField(max_length=40)    
    reportedCases = models.CharField(max_length=40) 
    """
    currentlyInfected = models.CharField(max_length=40)    
    infectionsByRequestedTime = models.CharField(max_length=40)  
    severeCasesByRequestedTime = models.CharField(max_length=40)
    hospitalBedsByRequestedTime = models.IntegerField()
    casesForICUByRequestedTime = models.IntegerField()
    casesForVentilatorsByRequestedTime = models.IntegerField()
    dollarsInFlight = models.IntegerField()
    """
        
    
    def __str__(self):
        return self.name
