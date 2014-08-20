from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from .Batch_Submit_Jobs_Dev import API_submit
 
from forms import UploadFileForm
from models import UploadFile
# Create your views here.

 
def home(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            new_file = UploadFile(file = request.FILES['file'])
            new_file.save()
          #  jobs_list = API_submit(new_file)
            ##this will be a list of dicts of jobs
 
            #return HttpResponseRedirect(reverse('main:home'))
            return HttpResponse("test")
    else:
        form = UploadFileForm()
 
    data = {'form': form}
    return render_to_response('main/index.html', data, context_instance=RequestContext(request))
    #return HttpResponse("test")

def response(request):
    pass
    #show response table
    #link to OVS packager job list
    