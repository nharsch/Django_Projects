from django.db import models
import OVSPackager_CLItools as CLI
#from csvimport.models import CSVimport
# Create your models here.
 
 
class UploadFile(models.Model):
    file = models.FileField(upload_to='files/%Y/%m/%d')

class PackJob(models.Model):
    prodid = models.CharField(max_length=12)
    title = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    asset_type = models.CharField(max_length=10) #consider making this a choice field
    priority = models.IntegerField(unique=False) 
    response = models.CharField(max_length=300, default="none - not yet submitted")
    # def __init__(self):
    #     self.response = "not submitted"
    def __unicode__(self):
        return self.name
    def is_packaged(self):
        return CLI.is_packaged(self.prodid)
    def is_in_queue(self):
        return CLI.is_in_queue(self.prodid)    
    def package(self):
        if self.is_in_queue():
            self.response = "already in packager queue"
        elif self.is_packaged():
            self.response = "already packaged"
        else:
            job_dict = {}
            job_dict['prod_id'] = self.prod_id
            job_dict['title'] = self.title
            job_dict['asset_type'] = self.asset_type
            job_dict['priority'] = self.priority
            submitter = CLI.submit_job(job_dict)

            self.response = submitter['response']
                # print self.response   
            # return self   
    ##column1=prodid, column2=title, column3=asset_type, column4=priority

class BatchJob(models.Model):
    name = models.CharField(max_length=400)
    job_list = models.ManyToManyField(PackJob) #should hold packjob objects
    def __unicode__(self):
        return self.name
    def package(self):
        for job in self.job_list.all():
            job.package()

