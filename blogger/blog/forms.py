from django import forms
from .models import BlogPost

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'slug']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter your title'}),
            'slug': forms.TextInput(attrs={'placeholder': 'URL-friendly slug'}),
            'content': forms.Textarea(attrs={'placeholder': 'Write your post content...'}),
        }
