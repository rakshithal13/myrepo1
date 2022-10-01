from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from myapp.forms import signupForm
from django.http import HttpResponseRedirect

# Create your views here.
def home_view(request):
    return render(request,'myapp/home.html')

@login_required
def java_view(request):
    return render(request,'myapp/javaexams.html')

def python_view(request):
    return render(request,'myapp/pythonexams.html')

def aptitude_view(request):
    return render(request,'myapp/aptitudeexams.html')

def logout_view(request):
    return render(request,'myapp/logout.html')

def signup_view(request):
    form=signupForm()
    if request.method=="POST":
        form=signupForm(request.POST)
        if form.is_valid():
            User=form.save()
            User.set_password(User.password)
            User.save()
            return HttpResponseRedirect('/accounts/login')
    d={'form':form}
    return render(request,'myapp/signup.html',d)
