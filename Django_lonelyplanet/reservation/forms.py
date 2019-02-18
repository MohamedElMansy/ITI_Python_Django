from django import forms

from .models import car,hotel

LOCATIONS = []

HOTELS = []

PERSONS = [
    ('1', '1 Adult'),
    ('2', '2 Adults'),
    ('3', '3 Adults'),
    ('4', '4 Adults')
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

class HotelForm(forms.ModelForm):
    class Meta:
        model = hotel
        fields = ['from_date','hotels','to_date','person_number']
        widgets = {
            'from_date': forms.DateTimeInput(attrs={'placeholder':'From','id': 'datepicker1','width':'200px'}),
            'to_date': forms.DateTimeInput(attrs={'placeholder':'To','id': 'datepicker2','width':'200px'}),
            'hotels':forms.Select(choices=HOTELS,attrs={'class':'form-control'}),
            'person_number':forms.Select(choices=PERSONS,attrs={'class':'form-control'})
        }

        
