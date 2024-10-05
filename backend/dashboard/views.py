from django.contrib.auth import logout, authenticate, login
from django.http import JsonResponse
from django.shortcuts import render, redirect


def dashboard_view(request):
    return render(request, 'dashboard/index.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'success': True, 'message': 'Login successful'}, status=200)
        else:
            return JsonResponse({'success': False, 'message': 'Invalid credentials'}, status=401)
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=400)


def check_login_status(request):
    return JsonResponse({'isAuthenticated': request.user.is_authenticated})


# Logout view
def user_logout(request):
    logout(request)
    return redirect('dashboard')
