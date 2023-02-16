from django import forms
from .models import Notes, Homework, ToDo
from django.core.exceptions import ValidationError
import datetime

# Notes Form !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class NotesForm(forms.ModelForm):
     class Meta:
        model = Notes
        fields = {'title','decriptions'}


# Homework Form !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
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
   

# Search Form !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class SearchForm(forms.Form):
   text = forms.CharField(max_length=100,label='Enter your Search',widget=forms.TextInput(attrs={'placeholder':'Enter your Search'}))


# TO DO Form !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class ToDoForm(forms.ModelForm):
   class Meta:
      model = ToDo
      fields = ('title','status')


# Conversion Form !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
MASS_UNITS = (
    ('g', 'Grams'),
    ('kg', 'Kilograms'),
    ('lbs', 'Pounds'),
    ('oz', 'Ounces'),
    
)

class MassConversionForm(forms.Form):
   value = forms.FloatField(label='Value', min_value=0)
   from_unit = forms.ChoiceField(label='From', choices=MASS_UNITS)
   to_unit = forms.ChoiceField(label='To', choices=MASS_UNITS)



TEMP_UNITS = (
    ('d', 'Degree'),
    ('f', 'Fahrenheit'),
    ('k', 'Kelvin'),
)

class TempConversionForm(forms.Form):
   value = forms.FloatField(label='Value', min_value=0)
   from_unit = forms.ChoiceField(label='From', choices=TEMP_UNITS)
   to_unit = forms.ChoiceField(label='To', choices=TEMP_UNITS)
