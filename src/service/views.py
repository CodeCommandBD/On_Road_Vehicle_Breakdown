from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'title': "Home",
    }
    return render(request, 'website/hello-project.html', context)