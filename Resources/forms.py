from django import forms
from .models import Lecture, Video


class AddLectureForm(forms.ModleForm):
    class Meta:
        model = Lecture
        fields = ['number', 'lecture_date']

class AddVideoForm(models.ModelForm):
    class Meta:
        model = Video
        fields = ['embede']