from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
import uuid
# Create your models here.

class Lesson(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=300)
	lesson_detail = RichTextField()
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lesson_owner')


	def __str__(self):
		return self.title
