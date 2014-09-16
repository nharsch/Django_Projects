import requests
import json
import time
from datetime import datetime, timedelta, date

client = requests.session()
client.stream = False
client.keep_alive = False
login_page = client.get('http://ovspackager.indemand.com/login/')
csrftoken = client.cookies['csrftoken']
resp = client.post('http://ovspackager.indemand.com/login/', {'username': 'nharsch', 'password': 'boat456', 'csrfmiddlewaretoken': csrftoken})

# Authentication


# Creating a new Package Job
# Four fields are required:
#   title
#   prod_id: iNDAB Prod ID
#   asset_type:  Movie: 1, Episode: 3 or Season: 2
#   priority: Any integer from 1-99. Lower numbers are higher priority. Default=50
#
# payload = {"title": "title", "prod_id": "0000000", "asset_type": "3", "priority": "5"}
# r = client.post("http://ovspackager.indemand.com/api/jobs/", data=json.dumps(payload))
# print r.text

# Polling for existing Package Jobs
# Returns the list of all Package Jobs
#r = client.get("http://ovspackager.indemand.com/api/jobs/")
#print r.text

# # You can filter jobs based on creation date and prod_id
# # Date format is "YYYY-MM-DD"
# # Filters can be combined together to form an "AND" filter

# # Filter by prod_id
# payload = {"prod_id": "451995"}
# r = client.get("http://ovspackager.indemand.com/api/jobs/", data=json.dumps(payload))

# # Filter by date range
# payload = {"start_date": "2014-06-01", "end_date": "2014-06-30"}
# r = client.get("http://ovspackager.indemand.com/api/jobs/", data=json.dumps(payload))

# # All jobs after a date
# payload = {"start_date": "2014-06-01"}
# r = client.get("http://ovspackager.indemand.com/api/jobs/", data=json.dumps(payload))

# # Get a specific Package Job
# r = client.get("http://ovspackager.indemand.com/api/jobs/1")
# print r.text

# # Delete a specific Package Job
# # The Job must be in either the 'Queue' or 'Error' state to be deleted
# r = client.delete("http://ovspackager.indemand.com/api/jobs/1")
# print r.text


def poll_all_jobs():
	r = client.get("http://ovspackager.indemand.com/api/jobs/")
	# print r.text
	return r.json()['objects']

def poll_all_jobs_month(date):
	"""date is YYYY-MM-DD"""
	#see if I can import date and automatically check from one month back from NOW
	payload = {"start_date": date }
	r = client.get("http://ovspackager.indemand.com/api/jobs/", data=json.dumps(payload))
	# print r.text
	return r.json()['objects']

date_floor = datetime.now() - timedelta(days=90)
date_floor = date.isoformat(date_floor)
all_jobs = poll_all_jobs_month(date_floor)

def poll_all_packaged():
	# date_floor = datetime.now() - timedelta(days=30)
	# date_floor = date.isoformat(date_floor)
	# print date_floor
	payload = {"is_packaged": True}
	r = client.get("http://ovspackager.indemand.com/api/jobs/", data=json.dumps(payload))
	# print r.text
	return r.json()['objects'] #return list of dicts

# all_packaged = poll_all_packaged()

def is_packaged(prod_id):
	# print "Searching for: ", prod_id
	prod_id = str(prod_id)
	for job in all_jobs:
		if str(job['prod_id']) == prod_id and job['is_packaged'] == True:
			# print job
			return True
	else:
		return False

def poll_all_inque():
	date_floor = datetime.now() - timedelta(days=3)
	date_floor = date.isoformat(date_floor)
	# print date_floor
	payload = {"start_date": date_floor ,"status": "In Queue"}
	r = client.get("http://ovspackager.indemand.com/api/jobs/", data=json.dumps(payload))
	# print r.text
	return r.json()['objects'] #return list of dicts

# all_inque = poll_all_inque()

def is_in_queue(prod_id):
	for job in all_jobs:
		if str(job['prod_id']) == str(prod_id) and job['status'] == "In Queue":
			# print job
			return True
	else:
		return False

def get_packID(prod_id):
	prod_id = str(prod_id)
	payload = {"prod_id": prod_id}
	r = requests.get("http://ovspackager.indemand.com/api/jobs/", data=json.dumps(payload))
	# print r.text
	return str(r.json()['objects'][0]['id'])

def get_status(prod_id):
	# print "Searching for: ", prod_id
	prod_id = str(prod_id)
	payload = {"prod_id": prod_id}
	r = client.get("http://ovspackager.indemand.com/api/jobs/", data=json.dumps(payload))
	# print "search response stat:", r.status_code
	# print "search response headers:", r.headers
	# r.connection.close()
	# print r.text
	# print str(r.json()['objects'][0]['status'])
	if len(r.json()['objects']) > 0:
		# print len(r.json()['objects'])
		status = str(r.json()['objects'][0]['status'])
		# r.json()['objects'] = []
		return status
	else:
		return False
		#not true if not in packager




def submit_job(job): #accepts a dict as payload
	# print "submit_job returns", get_status(job['prod_id'])

	#check if in queue
	if is_packaged(job['prod_id']):
		job['response'] = "NOT SUBMITTED: Job Already Packaged"
	if is_in_queue(job['prod_id']):
		job['response'] = "NOT SUBMITTED: Job Already In Queue"
	else:
		r = client.post("http://ovspackager.indemand.com/api/jobs/", data=json.dumps(job))
		response = r.text
		job['response'] = response #add response text to dict
	# print job
	return job
		#print job.values()


def submit_jobobj(jobobj):
		#check if in queue
	job_dict = {}
	job_dict['prod_id'] = jobobj.prod_id
	job_dict['title'] = jobobj.title
	job_dict['asset_type'] = jobobj.asset_type
	job_dict['priority'] = jobobj.priority

	submitter = submit_job(job_dict)

	jobobj.response	= submitter['response']
	print jobobj.response	
	return jobobj	
#tester = get_packID(98324)
#print tester


def job_delete(packID):
	packID = str(packID)
	r = client.delete("http://ovspackager.indemand.com/api/jobs/"+packID)
	print r.text



if __name__ == '__main__':

	# Make sure you get a '200' status code
	print "Login Response Code: ", resp.status_code, "\n"

	date_floor = datetime.now() - timedelta(days=3)
	date_floor = date.isoformat(date_floor)
	print date_floor
	# print poll_all_inque()


	# print get_status('999999') #bad
	# # time.sleep(1)
	# print is_in_queue('90013')  #error stat
	# print poll_all_packaged()
	# print get_status('423551') #error stat

	# # print all_packaged
	# print is_packaged('89518')
	# # print all_packaged
	# # print all_inque
	# print is_in_queue('89518')
	# submit_job('89518')

	# payload = {"prod_id": '90386'}
	# r = client.get("http://ovspackager.indemand.com/api/jobs/", data=json.dumps(payload))
	# print r.text, "\n"

	# payload = {"prod_id": '423551'}
	# n = client.get("http://ovspackager.indemand.com/api/jobs/", data=json.dumps(payload))
	# print n.text, "\n"

	# url = "http://ovspackager.indemand.com/api/jobs/"

	# print poll_all_jobs_month("2014-09-01")
	# print get_status('010101')