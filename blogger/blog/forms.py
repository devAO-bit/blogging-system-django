from django import forms
from .models import BlogPost

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'slug', 'cover_image', 'category', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter your title'}),
            'slug': forms.TextInput(attrs={'placeholder': 'URL-friendly slug'}),
            'content': forms.Textarea(attrs={'placeholder': 'Write your post content...'}),
            'cover_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'tags': forms.CheckboxSelectMultiple(),
        }
