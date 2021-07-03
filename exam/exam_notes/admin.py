from django.contrib import admin

# Register your models here.
from exam.exam_notes.models import NoteModel

admin.site.register(NoteModel)