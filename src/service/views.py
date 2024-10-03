from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'title': "Home",
    }
    return render(request, 'website/hello-project.html', context)

def userSignUp(request):
    context = {
        'title': "Sign Up",
    }
    return render(request, 'website/sign-up.html', context)

def userLogin(request):
    context = {
        'title': "Login",
    }
    return render(request, 'website/login.html', context)

def serviceModel(request):
   return render(request, 'website/service-model.html')