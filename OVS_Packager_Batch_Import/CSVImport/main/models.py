from django.db import models
#from csvimport.models import CSVimport
# Create your models here.
 
 
class UploadFile(models.Model):
    file = models.FileField(upload_to='files/%Y/%m/%d')

class PackJob(models.Model):
  	prodid = models.IntegerField(unique=False)
	title = models.CharField(max_length=300)
	asset_type = models.IntegerField() #consider making this a choice field
	priority = models.IntegerField() 
        def __unicode__(self):
            return self.title
    ##column1=prodid, column2=title, column3=asset_type, column4=priority

class BatchJob(models.Model):
    name = models.CharField(max_length=400)
    job_list = models.ManyToManyField(PackJob) #should hold packjob objects
    def __unicode__(self):
        return self.name