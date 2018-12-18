from django import forms
from django.forms import ModelForm
from .models import Post
from .models import Entry

class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ('comment', )

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'tag', 'published_date')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].widget.attrs.update({'class': 'textarea', 'placeholder': 'Add your comment.'})