from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Site
from .forms import SiteForm
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


def site_list(request):
    try:
        site = Site.objects.get()  # Get the single site object
    except Site.DoesNotExist:
        return redirect('site_create')  # Redirect to create if no site exists
    return render(request, 'dashboard/site.html', {'site': site})


def site_create(request):
    if Site.objects.exists():
        return redirect('site_update')
    if request.method == 'POST':
        form = SiteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('site_list')
    else:
        form = SiteForm()
    return render(request, 'dashboard/site_create_update.html', {'form': form})

# Update the existing Site
def site_update(request):
    site = get_object_or_404(Site)
    if request.method == 'POST':
        form = SiteForm(request.POST, request.FILES, instance=site)
        if form.is_valid():
            form.save()
            return redirect('site_list')
    else:
        form = SiteForm(instance=site)
    return render(request, 'dashboard/site_create_update.html', {'form': form})

