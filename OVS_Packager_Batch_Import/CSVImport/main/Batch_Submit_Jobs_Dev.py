#Batch Submit Jobs
import requests
import json
import csv


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
#     client = requests.session()
#     login_page = client.get('http://ovspackager.indemand.com/login')
#     csrftoken = client.cookies['csrftoken']
#     resp = client.post('http://ovspackager.indemand.com/login/', {'username': 'nharsch', 'password': 'boat456', 'csrfmiddlewaretoken': csrftoken})

# def header_to_fieldnames(csv_name):
# 	header_list = []
# 	with open(csv_name, 'rb') as csvfile:
# 		reader = csv.reader(csvfile)
# 		for i in reader.next():
# 			header_list.append(i)
# 		return header_list

    header_list = ['prod_id', 'title', 'asset_type', 'priority']
    
    jobs_list = [] #will be a list of row dicts to be passed to packager API one by one

    for i in csv_to_dictreader(csv_file, header_list):
        #print type(i['asset_type'])
        if i['asset_type'].lower() == "movie":
            i['asset_type'] = 1
        elif i['asset_type'].lower() == "season":
            i['asset_type'] = 2
        elif i['asset_type'].lower() == "episode":
            i['asset_type'] = 3
        jobs_list.append(i)

    return jobs_list

    #print jobs_list

    #post jobs to API
   # for job in jobs_list:
#         r = client.post("http://ovspackager.indemand.com/api/jobs/", data=json.dumps(job))
#         response = r.text
#         job['response'] = response #add response text to dict
        #print response
        #print job.values()
   

#    header_list.append('response')

    


    #write response on CSV
#     csv_output = csv_file.__unicode__[:-4]+"_RESPONSE.csv"

#     dictreader_to_csv(jobs_list, header_list, csv_output)







