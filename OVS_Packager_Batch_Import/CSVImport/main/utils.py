#Batch Submit Jobs
import requests
import json
import csv
import datetime
import OVSPackager_CLItools

from models import PackJob, BatchJob

def csv_to_dictreader(csv_file, header_list):
	'''
	takes file path
	returns dictreader object
	'''
# 	csv_file = open(csv_file, 'rb') #opens file
	dict_reader = []
	#make batch dict friendlier to write on
	for row in csv.DictReader(csv_file, header_list, dialect = 'excel'):
		dict_reader.append(row)

	return dict_reader

# def dictreader_to_csv(dict_reader, fieldnames, csv_output):
# 	with open(csv_output, 'wb') as csvfile:
# 		writer = csv.DictWriter(csvfile, fieldnames, delimiter = ',')
# 		writer.writeheader()
# 		for row in dict_reader:
# 			writer.writerow(row)

def csv_to_job_list(csv_file):
    header_list = ['prodid', 'title', 'asset_type', 'priority']
    
    job_list = [] #will be a list of row dicts to be passed to packager API one by one

    for i in csv_to_dictreader(csv_file, header_list):
        #print type(i['asset_type'])
        if i['asset_type'].lower() == "movie":
            i['asset_type'] = 1
        elif i['asset_type'].lower() == "season":
            i['asset_type'] = 2
        elif i['asset_type'].lower() == "episode":
            i['asset_type'] = 3
        job_list.append(i)

    return job_list #list of dicts

def job_maker(job_dict): #takes a dict returns a job obj
    new_job = PackJob()
    new_job.prodid = job_dict['prodid']
    new_job.title = job_dict['title']

    new_job.asset_type = job_dict['asset_type']
    new_job.priority = job_dict['priority']
    new_job.save() #which creates id
    new_job.name = new_job.title+"_"+str(new_job.id)
    new_job.save()
    return new_job

def batch_maker(csv_file):
    batch_job = BatchJob()
    batch_job.name = csv_file.name+"_"+str(datetime.datetime.utcnow()) #see if this works
    batch_job.save()
    for jobdict in csv_to_job_list(csv_file): #for job dict in list of dicts
        job = job_maker(jobdict)
        batch_job.job_list.add(job) 
    batch_job.save()
    return batch_job

def batch_submitter(batch): #batch object
    for job in batch.job_list:
        job.submit()
    return batch