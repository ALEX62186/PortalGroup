from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    grade_class = models.CharField(max_length=20, help_text="Напр. 7А, 10Б")

    def __str__(self):
        return f"{self.last_name} {self.first_name} ({self.grade_class})"

class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="marks")
    subject = models.CharField(max_length=100)
    mark = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.subject}: {self.mark}"
