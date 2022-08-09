from django.urls import path
from classroom.views import Categories, CategoryCourses, NewCourse, Enroll, DeleteCourse, EditCourse, CourseDetail
from lesson.views import NewLesson, CourseLesson, DeleteLesson, EditLesson, DetailLesson
urlpatterns = [
	#Course - Classroom Views
	path('newcourse/', NewCourse, name='newcourse'),
	path('categories/', Categories, name='categories'),
	path('categories/<category_slug>', CategoryCourses, name='category-courses'),
	path('<course_id>/', CourseDetail, name='course'),
	path('<course_id>/enroll', Enroll, name='enroll'),
	path('<course_id>/edit', EditCourse, name='edit-course'),
	path('<course_id>/delete', DeleteCourse, name='delete-course'),
	path('<course_id>/lesson', CourseLesson, name='lesson'),
	path('<course_id>/lesson/newlesson', NewLesson, name='new-lesson'),
	path('<course_id>/lesson/<lesson_id>/delete', DeleteLesson, name='delete-lesson'),
	path('<course_id>/lesson/<lesson_id>/edit', EditLesson, name='edit-lesson'),
	path('<course_id>/lesson/<lesson_id>/view', DetailLesson, name='detail-lesson'),
]