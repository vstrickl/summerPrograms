from django import forms
from .models import Applicant


# Create your forms here.
class ApplicantsForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = [
            'parent_first_name',
            'parent_last_name',
            'child_first_name',
            'child_last_name', 
            'street_address',
            'city',
            'state',
            'zip_code',
            'email',
            'phone', 
            'send_email',
            'send_text',
            'need_financial_aid',
        ]

        widgets = {
            'parent_first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Parent\'s First Name',
                    'class':'form-control mb-3',
                }
            ),
            'parent_last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Parent\'s Last Name',
                    'class':'form-control mb-3',
                }
            ),
            'child_first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Child\'s First Name',
                    'class':'form-control mb-3',
                }
            ),
            'child_last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Child\'s Last Name',
                    'class':'form-control mb-3',
                }
            ),
            'street_address': forms.TextInput(
                attrs={
                    'placeholder': '123 Fouth Street',
                    'class':'form-control mb-3',
                }
            ),
            'city': forms.TextInput(
                attrs={
                    'placeholder': 'South San Francisco',
                    'class':'form-control mb-3',
                }
            ),
            'state': forms.TextInput(
                attrs={
                    'placeholder': 'CA',
                    'class':'form-control mb-3',
                }
            ),
            'zip_code': forms.TextInput(
                attrs={
                    'placeholder': '94080',
                    'class':'form-control mb-3',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email',
                    'class':'form-control mb-3',
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'placeholder': 'Phone',
                    'class':'form-control mb-3',
                }
            ),
            'send_email': forms.CheckboxInput(
                attrs={
                    'class':'form-check-input',
                }
            ),
            'send_text': forms.CheckboxInput(
                attrs={
                    'class':'form-check-input',
                }
            ),
            'need_financial_aid': forms.CheckboxInput(
                attrs={
                    'class':'form-check-input',
                }
            ),
        }
