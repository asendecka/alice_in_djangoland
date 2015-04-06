from django import forms
from .models import WorkDone


class WorkDoneForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')  
        super(WorkDoneForm, self).__init__(*args, **kwargs)

    def save(self):
        instance = super(WorkDoneForm, self).save(commit=False)
        instance.user = self.user
        instance.save()
 
    class Meta:
        model = WorkDone
        fields = ('project', 'minutes', 'description', )
