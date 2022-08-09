from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from lesson.models import Lesson
from lesson.forms import NewLessonForm
from classroom.models import Course
from django.contrib.auth.decorators import login_required

@login_required
def CourseLesson(request, course_id):
	user = request.user
	course = get_object_or_404(Course, id=course_id)
	teacher_mode = False
	if user == course.user:
		teacher_mode = True

	context = {
		'teacher_mode': teacher_mode,
		'course': course,
	}

	return render(request, 'lesson/lesson.html', context)

@login_required
def NewLesson(request, course_id):
	user = request.user
	course = get_object_or_404(Course, id=course_id)
	if request.method == 'POST':
		form = NewLessonForm(request.POST)
		if form.is_valid():
			title = form.cleaned_data.get('title')
			description = form.cleaned_data.get('description')
			lesson_detail = form.cleaned_data.get('lesson_detail')
			m = Lesson.objects.create(title=title, description=description, lesson_detail=lesson_detail, user=user)
			course.lesson.add(m)
			course.save()
			return redirect('lesson', course_id=course_id)
	else:
		form = NewLessonForm()
	context = {
		'form': form,
	    }
	return render(request, 'lesson/newlesson.html', context)

@login_required
def DeleteLesson(request, lesson_id, course_id):
	user = request.user
	lesson= get_object_or_404(Lesson, id=lesson_id)

	if user != lesson.user:
		return HttpResponseForbidden()
	else:
		lesson.delete()
	return redirect('lesson', course_id=course_id)

@login_required
def EditLesson(request, course_id, lesson_id ):
	user = request.user
	lesson= get_object_or_404(Lesson, id=lesson_id)

	if user != lesson.user:
		return HttpResponseForbidden()

	else:
		if request.method == 'POST':
			form = NewLessonForm(request.POST, request.FILES, instance=lesson)
			if form.is_valid():
				lesson.title = form.cleaned_data.get('title')
				lesson.description = form.cleaned_data.get('description')
				lesson.lesson_detail = form.cleaned_data.get('lesson_detail')
				form.save()
				return redirect('lesson', course_id=course_id)
		else:
			form = NewLessonForm(instance=lesson)

	context = {
		'form': form,
		'lesson': lesson
	}

	return render(request, 'lesson/editlesson.html', context)

@login_required
def DetailLesson(request, lesson_id,  course_id):
	lesson = get_object_or_404(Lesson, id=lesson_id)
	course = get_object_or_404(Course, id=course_id)

	context = {
		'lesson': lesson,
		'course': course,
		'course_id': course_id,

	}

	return render(request, 'lesson/lesson_detail.html', context)