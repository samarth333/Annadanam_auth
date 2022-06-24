from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Members
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse
# Create your views here.
 
def home(request):
    return render(request,"users/home.html")


def index(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))


def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    member = Members(firstname=x, lastname=y)
    member.save()
    return HttpResponseRedirect(reverse('index'))
