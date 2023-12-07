from django import forms
from .models import TeamMember

class TeamMemberForm(forms.ModelForm):
    ROLE_CHOICES = [
        (False, 'Regular - Cannot delete members'),
        (True, 'Admin - Can delete members'),
    ]

    role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.RadioSelect(attrs={'checked': 'checked'}))

    class Meta:
        model = TeamMember
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'role']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
        }
        labels = {
          
            'first_name': 'False',
            'last_name': False,
            'email': False,
            'phone_number': False,
            'role': 'Role',
        }
        role = forms.TypedChoiceField(
            choices=[(True, 'member'), (False, 'admin')],
            coerce=lambda x: x == 'True',
            widget=forms.RadioSelect(attrs={'checked': 'checked'})
        )
