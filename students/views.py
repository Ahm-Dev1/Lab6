from django.shortcuts import render ,redirect
from django.db import models

class Student(models.Model):
    student_name = models.CharField(max_length=50)
    student_age = models.IntegerField()
    student_email = models.EmailField()
    student_address = models.CharField(max_length=100)
    courses = models.ManyToManyField('Course', related_name='students')

class Course(models.Model):
    course_name = models.CharField(max_length=50)
    course_description = models.TextField()
    course_price = models.DecimalField(max_digits=5, decimal_places=2)


#students path
def students(request):
    students = Student.objects.all()
    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_age = request.POST.get('student_age')
        student_email = request.POST.get('student_email')
        student_address = request.POST.get('student_address')
        student = Student.objects.create(
            student_name=student_name,
            student_age=student_age,
            student_email=student_email,
            student_address=student_address
        )
        return redirect('students')
    return render(request, 'students.html', {'students':students})

#details path
def details(request, student_id):
    student = Student.objects.get(id=student_id)
    courses = Course.objects.all()
    if request.method == 'POST':
        course_id = request.POST.get('course')
        student.courses.add(course_id)
        student.save()
    return render(request, 'details.html', {'student':student, 'courses':courses})

#courses path
def courses(request):
    courses = Course.objects.all()
    if request.method == 'POST':
        course_name = request.POST.get('course_name')
        course_description = request.POST.get('course_description')
        course_price = request.POST.get('course_price')
        course = Course.objects.create(
            course_name=course_name,
            course_description=course_description,
            course_price=course_price
        )
        return redirect('courses')
    return render(request, 'courses.html', {'courses':courses})
