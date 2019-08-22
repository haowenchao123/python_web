import os
from django.http import HttpResponse
from app.forms import MomentForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render


def welcome(request):
    return HttpResponse("<h1>Welcome to my tiny twitter!</h1>")


def moments_input(request):
    if request.method == 'POST':
        form = MomentForm(request.POST)
        if form.is_valid():
            moment = form.save()
            moment.save()
            return HttpResponseRedirect(reverse("first-url"))
    else:
        form = MomentForm()
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return render(
        request,
        os.path.join(PROJECT_ROOT, 'app/templates', 'moments_input.html'),
        {'form': form})

def current_datetime(request):
	now = datetime.datatime.now().strftime("%Y-%m-%d %H: %M: %S")
	return HttpResponse(now)

def detail(request, moment_id):
	m = Moment.object.get(id=moment_id)
	return render(request, 'templates/moment.html', {'headline': m.headline, 'user': m.user_name})

def my_view(request):
#	return HttpResponseNotFound()
	return HttpResponse(status=404)

def view_moment(request):
	data = {'content': 'Please input the content', 'user_name': '匿名', 'kind':'Python技术'}
	f = MomentForm(request.POST, initial = data)
	if f.has_changed():
		print("如下字段进行了修改: ")
		for field in f.changed_data:
			print(field)

