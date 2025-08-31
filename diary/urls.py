from django.urls import path
from . import views

urlpatterns = [
    path("", views.diary_view, name="diary"),

    # Ученики
    path("student/add/", views.add_student, name="add_student"),
    path("student/<int:student_id>/edit/", views.edit_student, name="edit_student"),
    path("student/<int:student_id>/delete/", views.delete_student, name="delete_student"),

    # Оценки
    path("mark/add/", views.add_mark, name="add_mark"),
    path("mark/<int:mark_id>/edit/", views.edit_mark, name="edit_mark"),
    path("mark/<int:mark_id>/delete/", views.delete_mark, name="delete_mark"),
]
