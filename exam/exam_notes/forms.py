from django import forms

from exam.exam_notes.models import NoteModel


class NoteForm(forms.ModelForm):
    class Meta:
        model = NoteModel
        fields = '__all__'

class DeleteNoteForm(NoteForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)
        for (_,field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'