from django import forms

from apps.posts.models import Post


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'source']

    def __init__(self, *args, **kwargs):
        super(NewPostForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = 'Título'
        self.fields['source'].widget.attrs['placeholder'] = 'Font (opicional)'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'py-3 outline-blue-500 focus:ring-blue-500  focus:border-blue-500 rounded-md indent-4 bg-gray-100 ring-[1px] ring-gray-500 ring-opacity-40 dark:bg-darkInput dark:text-white'
            if field == 'description':
                self.fields[field].widget.attrs['class'] = 'py-3 resize-none w-full h-[500px] outline-blue-500 focus:ring-blue-500 focus:border-blue-500 rounded-md  bg-gray-100 ring-[1px] ring-gray-500 ring-opacity-40 dark:bg-darkInput dark:text-white p-4'


class NewCommentForm(forms.Form):
    description = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Comente algo'}))

    def __init__(self, *args, **kwargs):
        super(NewCommentForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field == 'description':
                self.fields[field].widget.attrs['class'] = 'py-3 resize-none w-full outline-blue-500 focus:ring-blue-500 focus:border-blue-500 rounded-md  bg-gray-100 ring-[1px] ring-gray-500 ring-opacity-40 dark:bg-darkInput dark:text-white p-4'
