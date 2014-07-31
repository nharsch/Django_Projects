from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
	# Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am the bold font from the context"}
    return render_to_response('rango/index.html', context_dict, context)




# Create your views here.
