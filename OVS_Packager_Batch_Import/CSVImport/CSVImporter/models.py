from django.db import models

# Create your models here.
class PackJob(models.Model):
	prodid = models.IntegerField(max_length= 8)
	title = models.CharField(max_length=144)
	asset_type = models.IntegerField(max_length= 1) #consider making this a choice field
	priority = models.IntegerField(max_length= 2) 
  ## possibly add "job_types = (package, delete...)"


