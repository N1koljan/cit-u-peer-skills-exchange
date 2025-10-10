from django import forms
from core.models import CustomUser # Import your CustomUser model from the 'core' app

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'school_id', 'department', 'bio', 'profile_picture')

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'school_id': forms.TextInput(attrs={'placeholder': 'School ID'}),
            'department': forms.Select(), # This will render as a dropdown
            'bio': forms.Textarea(attrs={'placeholder': 'Write something about yourself...', 'rows': 4}),
            'profile_picture': forms.FileInput(),
        }