from django import forms
from blogapp.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name','email','Description')
