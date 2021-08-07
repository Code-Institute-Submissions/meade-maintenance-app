from django import forms
from django.forms.widgets import SplitDateTimeWidget
from .models import Job, JobStatus, JobPriority, JobTimes, JobTypes, JobSteps
from ancillaries.models import Departments
from datetime import datetime, timedelta

class JobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = [
            'job_title',
            'department',
            'type',
            'priority',
            'description',
            'project',
            'assigned_to',
            'created_by',
        ]
    
    def __init__(self, *args, **kwargs):
        self.profile = kwargs.pop('profile')
        super(JobForm, self).__init__(*args, **kwargs)
        self.fields['created_by'].initial = self.profile.user.id
        self.fields['created_by'].widget.attrs['hidden'] = True
        self.fields['created_by'].label = ""

        if not str(self.profile.user_type).lower() in ('admin', 'manager'):
            self.fields['assigned_to'].initial = self.profile.user.id
            self.fields['assigned_to'].widget.attrs['hidden'] = True
            self.fields['assigned_to'].label = ""


class JobStepsForm(forms.ModelForm):

    class Meta:
        model = JobSteps
        fields = ['job', 'step_number', 'step']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class JobTimesForm(forms.ModelForm):
    
    class Meta:
        model = JobTimes
        exclude = ['job']
    
    time_start = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(),
        initial=datetime.now()
    )
    time_end = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(),
        initial=datetime.now() + timedelta(hours=1)
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

