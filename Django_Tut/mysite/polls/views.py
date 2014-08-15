from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from polls.models import Choice, Poll

# from django.template import RequestContext, loader

from polls.models import Poll

# Create your views here.
def index(request):
	# return HttpResponse("Hello, world. You're at the poll index.")
	#this is the simplest view possible in Django. 
	#To call view, we need to map it to a URL = and for this we need a URLconf

	# latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
	# template = loader.get_template('polls/index.html')
	# context = RequestContext(request, {
	# 	'latest_poll_list': latest_poll_list,
	# })
	# # output = ', '.join([p.question for p in latest_poll_list])
	# return HttpResponse(template.render(context))

	latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
	context = {'latest_poll_list': latest_poll_list}
	return render(request, 'polls/index.html', context)

def detail(request, poll_id):
	# try:
	# 	poll = Poll.objects.get(pk=poll_id)
	# except Poll.DoesNotExist:
	# 	raise Http404
	# return render(request, 'polls/detail.html', {'poll': poll})

	poll = get_object_or_404(Poll, pk=poll_id)
	return render(request, "polls/detail.html", {'poll':poll})

def results(request, poll_id):
	return HttpResponse("You're looking at the results of poll %s. " % poll_id)

def vote(request, poll_id):
	p = get_object_or_404(Poll, pk=poll_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# REdisplay the poll voting form.
		return render(request, 'polls/detail.html', {
			'poll': p, 
			'error_message': "You didn't select a choice.",
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
	return HttpREsponse("You're voting on poll %s." % poll_id)

