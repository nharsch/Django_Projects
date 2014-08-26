from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from .utils import csv_to_job_list, batch_maker
from main.models import PackJob, BatchJob

from forms import UploadFileForm
from models import UploadFile
# Create your views here.

 
def home(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES) # form bound to post data
        if form.is_valid():
            new_file = UploadFile(file = request.FILES['file'])
            new_file.save()
            batch_job = batch_maker(request.FILES['file']) #builds packjob and jobs, returns BatchJob object
#             job_id = str(batch_job.id)
            
            ##this will be a list of dicts of jobs
            #return HttpResponseRedirect(reverse('main:home'))
#             return HttpResponse(jobs_list)
#             return render_to_response('main/batchview.html')
            return HttpResponseRedirect(reverse('main:batchview', args=(batch_job.id,)))
    else:
        form = UploadFileForm()
        data = {'form': form}
    
    return render_to_response('main/index.html', data, context_instance=RequestContext(request))
    #return HttpResponse("test")

def batchview(request, batch_id):
#     return HttpResponse('test')
#     if request.method =='POST':
    batch_job = get_object_or_404(BatchJob, pk=batch_id)
    return render_to_response('main/batchview.html', {'batch_job' : batch_job})
#     return HttpResponse("Your're looking at the contents of batch %s." % batch_id)
#     job_list = request.body
#     context = {'batch_id' : batch_id}
#     return render_to_response('main/batchview.html')
    
    