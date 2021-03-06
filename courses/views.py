from django.shortcuts import render
from .models import Speciality
from django.http import HttpResponse
from .models import Teacher
from .models import Subject
from .forms import SpecialityForm
from .forms import TeacherForm
from .forms import SubjectForm


def subject_view(request):
    subjects = Subject.objects.all()
    return render(request, "courses/subject.html", {
        "subjects": subjects,
    })


def teacher_view(request):
    search = request.GET.get("search")

    if search is None:
        teachers = Teacher.objects.all()
    else:
        teachers = Teacher.objects.filter(first_name__contains=search)
    return render(request, "courses/teacher.html", {
        "teachers": teachers, "search": search,
    })


def speciality_view(request):
    speciality = Speciality.objects.all()
    if speciality is None:
        speciality = request.GET.get("No speciality")
        return HttpResponse(f"{speciality,}")
    else:
        return render(request, "courses/speciality.html", {
            "speciality": speciality,
        })


def speciality_create(request):
    if request.method == 'GET':
        form = SpecialityForm()
    else:
        form = SpecialityForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Speciality.objects.create(
                name=data['name'],
                code=data['code'],
                stat_data=data['stat_data'],
                is_active=data['is_active'],
            )
    return render(request, 'courses/speciality_create.html', {
        "form": form,
    })


def teacher_create(request):
    if request.method == 'GET':
        form = TeacherForm()
    else:
        form = TeacherForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Teacher.objects.create(
                first_name=data['first_name'],
                last_name=data['last_name'],
                degree=data['degree'],
            )
    return render(request, 'courses/teacher_create.html', {
        "form": form,
    })


def subject_create(request):
    if request.method == 'GET':
        form = SubjectForm()
    else:
        form = SubjectForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Subject.objects.create(
                name=data['name'],
                Specialities=data['Specialities'],
                teachers=data['teachers'],
            )
    return render(request, 'courses/subject_create.html', {
        "form": form,
    })

