from django import forms
from django.contrib.auth.forms import UserCreationForm
from.models import SignUpUser

class SignUpCreationForm(UserCreationForm):

    class Meta:
          model = SignUpUser
          fields = ('username', 'email','first_name', 'last_name')

    def save(self, commit=True):
         user = super(SignUpCreationForm, self).save(commit=False)
         user.email = self.cleaned_data['email']
         user.first_name = self.cleaned_data['first_name']
         user.last_name = self.cleaned_data['last_name']

         if commit:
            user.save()

         return user