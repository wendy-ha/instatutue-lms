from django.urls import path
from lesson.views import NewLesson, CourseLesson
urlpatterns = [

	path('<lesson_id>/', CourseLesson, name='courselesson'),

]