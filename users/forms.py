from django.forms import ModelForm
from django import forms
from users.models import Accomplishment, Education, Experience

class AddExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['title', 'description', 'company', 'location', 'start_date', 'end_date', 'currently_working']


class AddAccomplishmentForm(forms.ModelForm):
    class Meta:
        model = Accomplishment
        fields = ['title', 'description', 'start_date', 'end_date', 'currently_working', 'visit_url']


class AddEducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['degree', 'subject', 'start_date', 'end_date', 'currently_studying', 'institution', 'description']