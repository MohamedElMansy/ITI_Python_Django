from django import forms

from .models import car

LOCATIONS = [
    ]

class CarForm(forms.ModelForm):
    class Meta:
        model = car
        fields = ['from_date','from_time','location','to_date','to_time']
        widgets = {
            'from_date': forms.DateTimeInput(attrs={'placeholder':'From','id': 'datepicker1','width':'200px'}),
            'from_time': forms.DateTimeInput(attrs={'placeholder':'From','id': 'timepicker1','width':'200px'}),
            'to_date': forms.DateTimeInput(attrs={'placeholder':'To','id': 'datepicker2','width':'200px'}),
            'to_time': forms.DateTimeInput(attrs={'placeholder':'To','id': 'timepicker2','width':'200px'}),
            'location':forms.Select(choices=LOCATIONS,attrs={'class':'form-control'})
        }

        

        
