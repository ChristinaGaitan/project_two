from django import forms
from app_two.models import User

# Extends ModelForm
class NewUserForm(forms.ModelForm):
  # Validations here

  class Meta:
    model = User
    fields = '__all__'
