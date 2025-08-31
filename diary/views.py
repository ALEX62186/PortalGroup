from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from .models import Student, Mark
from .forms import StudentForm, MarkForm

# ----------------- ЭЛЕКТРОННЫЙ ДНЕВНИК -----------------
def diary_view(request):
    students = Student.objects.all().prefetch_related("marks")
    return render(request, "diary/diary.html", {"students": students})

# ----------------- УЧЕНИКИ -----------------
@staff_member_required
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("diary")
    else:
        form = StudentForm()
    return render(request, "diary/student_form.html", {"form": form, "title": "Додати учня"})

@staff_member_required
def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("diary")
    else:
        form = StudentForm(instance=student)
    return render(request, "diary/student_form.html", {"form": form, "title": "Редагувати учня"})

@staff_member_required
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == "POST":
        student.delete()
        return redirect("diary")
    return render(request, "diary/confirm_delete_student.html", {"student": student})

# ----------------- ОЦЕНКИ -----------------
@staff_member_required
def add_mark(request):
    if request.method == "POST":
        form = MarkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("diary")
    else:
        form = MarkForm()
    return render(request, "diary/mark_form.html", {"form": form, "title": "Додати оцінку"})

@staff_member_required
def edit_mark(request, mark_id):
    mark = get_object_or_404(Mark, id=mark_id)
    if request.method == "POST":
        form = MarkForm(request.POST, instance=mark)
        if form.is_valid():
            form.save()
            return redirect("diary")
    else:
        form = MarkForm(instance=mark)
    return render(request, "diary/mark_form.html", {"form": form, "title": "Редагувати оцінку"})

@staff_member_required
def delete_mark(request, mark_id):
    mark = get_object_or_404(Mark, id=mark_id)
    if request.method == "POST":
        mark.delete()
        return redirect("diary")
    return render(request, "diary/confirm_delete_student.html", {"mark": mark})
