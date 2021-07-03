from django.shortcuts import render, redirect

from core.get_profile import get_profile
from exam.exam_notes.forms import NoteForm, DeleteNoteForm
from exam.exam_notes.models import NoteModel
from exam.exam_profile.models import ProfileModel


def home_page(request):
    profile = get_profile()
    notes = NoteModel.objects.all()
    if not profile:

        return redirect('create profile')

    context = {
        'profile': profile,
        'notes': notes,
    }

    return render(request,'home-with-profile.html',context)

def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = NoteForm()

    context = {
            'form': form,
        }
    return render(request,'note-create.html',context)


def edit_note(request,pk):
    note = NoteModel.objects.get(pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST,instance= note)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoteForm(instance= note)

    context = {
        'form': form,
        'note': note,
    }
    return render(request, 'note-edit.html', context)

def delete_note(request,pk):
    note = NoteModel.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteNoteForm(request.POST, instance=note)
        note.delete()
        return redirect('home')
    else:
        form = DeleteNoteForm(instance=note)

    context = {
        'form': form,
        'note': note,
    }
    return render(request, 'note-delete.html', context)

def note_details(request,pk):
    note = NoteModel.objects.get(pk=pk)
    notes = NoteModel.objects.all()
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoteForm(instance=note)

    context = {
        'form': form,
        'note': note,
        'notes': notes,
    }
    return render(request, 'note-details.html', context)
