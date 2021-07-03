from django import forms

from exam.exam_profile.models import ProfileModel


class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'