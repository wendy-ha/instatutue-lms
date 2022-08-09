from django import forms
from ckeditor.widgets import CKEditorWidget
from lesson.models import Lesson

class NewLessonForm(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(attrs={'class': 'validate'}), required=True)
	description = forms.CharField(widget=forms.TextInput(attrs={'class': 'validate'}), required=True)
	lesson_detail = forms.CharField(widget=CKEditorWidget())

	class Meta:
		model = Lesson
		fields = ('title', 'description', 'lesson_detail' )


