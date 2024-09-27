from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import render, redirect
# Create your views here.
def staff_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user.is_staff:
            login(request, user)
            return redirect('dashboard')
        else:
            return JsonResponse({'success': False}, status=400)
    return render(request, 'dashboard/auth-login-basic.html')