from django import forms 
from django.core import validators
# widget -> field to html input
class contactForm(forms.Form):
    name = forms.CharField(label='Full Name: ',help_text="Total length must be between 1 and 70 characters",required=False,widget=forms.Textarea(attrs={'id':'text_area','class':'class1 class2','placeholder':'Enter your name',}))
    # file = forms.FileField()
    # email = forms.EmailField(label="User Email")
    # age = forms.IntegerField(label="Age")
    # weight = forms.FloatField()
    age = forms.CharField(widget=forms.NumberInput)
    # sob gula te charField use kora jabe 
    balance = forms.DecimalField()
    check = forms.BooleanField()
    
    birthDate = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    appointment = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))
    CHOICES = [('S','Small'),('M','Medium'),('L','Large')]
    size = forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)
    
    MEAL = [('P','Pepperone'),('M','Mashroom'),('B','Beef')]
    pizza = forms.MultipleChoiceField(choices=MEAL,widget=forms.CheckboxSelectMultiple)
    
# class StudentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)
#     # def clean_name(self):
#     #     valName = self.cleaned_data['name']
#     #     if len(valName)<10:
#     #         raise forms.ValidationError("Please enter a name with at least 10 characters")
    
#     #     return valName
    
#     # def clean_email(self):
#     #     valEmail = self.cleaned_data['email']
#     #     if '.com' not in valEmail :
#     #        raise forms.ValidationError("Your email must contain '.com'")
       
#     #     return valEmail
#     def clean(self):
#         clean_data = super().clean()
#         valName = clean_data['name']
#         valEmail = clean_data['email']
        
#         if len(valName)<10:
#             raise forms.ValidationError("Please enter a name with at least 10 characters")
        
#         if '.com' not in valEmail :
#            raise forms.ValidationError("Your email must contain '.com'")
        
   
def check_len(value):
    if len(value) <10:
        raise forms.ValidationError("Please enter a name with at least 10 characters")
    
    
class StudentData(forms.Form):
    name = forms.CharField(widget=forms.TextInput,
        validators=[validators.MinLengthValidator(10, message="Please enter a name with at most 10 characters")]
    )
    text= forms.CharField(widget=forms.TextInput,validators=[check_len])
    email = forms.CharField(widget=forms.EmailInput,validators=[validators.EmailValidator(message="Please enter a valid email address")])
    age = forms.IntegerField(validators=[validators.MinValueValidator(24,message='Age must be at least  24'),validators.MaxValueValidator(34,message='Age must be maximum of 34')])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','png'])])
    
    
class PasswordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        clean_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_conpass = self.cleaned_data['confirm_password']
        val_name = self.cleaned_data['name']
        if val_pass != val_conpass:
            raise forms.ValidationError("Passwords doesn't match")   
        
        if len(val_name) <10:
            raise forms.ValidationError("Please enter a name with at least 10 characters")