from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from dashboard.decorators import staff_login_required


@staff_login_required
def dashboard(request):
    context = {
        'title': 'Dashboard'
    }
    return render(request, 'dashboard/dashboard.html', context)

@staff_login_required
def staff_logout(request):
    try:
        logout(request)
        return redirect('dashboard')
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)