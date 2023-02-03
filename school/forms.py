from .models import StudyMaterial
from django.forms import ModelForm, TextInput


class schoolForm(ModelForm):
    class Meta:
        model = StudyMaterial
        fields = '__all__'

        labels = {
            'name' : 'Name',
            'age' : 'Age',
            'subjectName' : 'Subject Name',
            'topic' : 'Topic',
            'image' : 'Image',
            'video' : 'Video'
        }
