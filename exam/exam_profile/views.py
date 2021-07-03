from django.shortcuts import render, redirect

from core.get_profile import get_profile
from exam.exam_notes.models import NoteModel
from exam.exam_profile.forms import ProfileForm
from exam.exam_profile.models import ProfileModel


def profile_page(request):
    profile = get_profile()
    notes = NoteModel.objects.all()
    if not profile:
        return redirect('create profile')
    else:
        context = {
            'notes': notes,
            'profile': profile,
        }
        return render(request,'profile.html',context)


def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = ProfileForm()

    context = {
        'form':form,
    }

    return render(request, 'home-no-profile.html', context)

def delete_user(request):
    user = ProfileModel.objects.first()

    if request.method == 'POST':
        user.delete()
        return redirect('home')
    else:
        form = ProfileForm()

    context = {
        'form': form,
    }

    return render(request, 'home-no-profile.html', context)

