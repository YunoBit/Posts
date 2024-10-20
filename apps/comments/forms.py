from django import forms

from apps.comments.models import Comments


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comments
        fields = ['text']