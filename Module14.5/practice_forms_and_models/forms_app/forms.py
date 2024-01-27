
from django import forms 
import datetime
# field_name = forms.FieldType(**options)


class PracticeForm(forms.Form):
    # each field would be mapped as an input field in HTML 
    title = forms.CharField(
        max_length = 10,
    )
    description= forms.CharField()
    first_name = forms.CharField(max_length=200,initial='Your name')
    roll_number = forms.IntegerField(help_text="Enter 6 digit roll number")
    password = forms.CharField(widget=forms.PasswordInput())
    
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    Email = forms.EmailField(
         required = False,
         label="Please enter your email address",
    )
    agree = forms.BooleanField(initial=True)
    
    date = forms.DateField()
    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    
    value = forms.DecimalField()
    day = forms.DateField(initial=datetime.date.today())
    
    FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
    ]
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_color2 = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    favorite_colors3 = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_colors4 = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES,)