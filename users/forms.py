from django import forms
from django import forms
from users.models import Profile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio', 'country']
