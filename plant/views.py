from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import PlantForm


def home(request):
    context = {
        'message': 'Welcome to django'
    }
    return render(request, 'plant/home.html', context)


def about(request):
    return render(request, 'plant/about.html')


@login_required
def uploadImage(request):
    if request.method == 'POST':
        p_form = PlantForm(request.POST, request.FILES)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'you have been uploaded image successfully!')
            return redirect('plant-home')
    else:
        p_form = PlantForm()
    context = {
        'p_form': p_form
    }
    return render(request, 'plant/upload_image.html', context)

@login_required
def remedy(request):
    return render(request, 'plant/remedies.html')



