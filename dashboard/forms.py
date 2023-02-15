from django import forms
from .models import Notes, Homework
from django.core.exceptions import ValidationError
import datetime

class NotesForm(forms.ModelForm):
     class Meta:
        model = Notes
        fields = {'title','decriptions'}

class DateInput(forms.DateInput):
   input_type='date'

class HomeworkForm(forms.ModelForm):
   class Meta:
      model = Homework
      widgets={'due':DateInput()}
      fields = ('subject','title', 'descriptions', 'due', 'is_finish', )
   
   def clean_due(self):
      cleaned_data = self.cleaned_data.get('due')
      local_date = datetime.date.today()
      form_date_str = str(cleaned_data).split(' ')[0]
      form_date = datetime.datetime.strptime(form_date_str, '%Y-%m-%d').date()

      if local_date > form_date:
            raise ValidationError('Due Date should be greator than today')
      return cleaned_data
   