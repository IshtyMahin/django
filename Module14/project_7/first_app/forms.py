from django import forms 
from first_app.models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        # exclude = ['roll']
        labels = {
            'roll': 'Student Roll',
            'name': 'Student Name',
            'father_name': 'Father Name',
            'address': 'Address'
        }
        widgets = {
            # 'name' : forms.TextInput(attrs={'class':'btn btn-primary'}),
            # 'roll': forms.PasswordInput()
            'name':forms.TextInput()
        }
        help_texts = {
            'name' : 'Write your full name',
        }
        error_messages= {
            'name': {"required":'Your name is required'}
        }