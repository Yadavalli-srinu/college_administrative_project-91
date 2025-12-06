from app1.models import department_model,hod_model,professor_model,student_model
from django import forms

class department_u_form(forms.ModelForm):
    class Meta:
        model=department_model
        fields='__all__'
    
class hod_u_form(forms.ModelForm):
    class Meta:
        model=hod_model
        fields='__all__'

class professor_u_form(forms.ModelForm):
    class Meta:
        model=professor_model
        fields='__all__'

class student_u_form(forms.ModelForm):
    class Meta:
        model=student_model
        fields='__all__'