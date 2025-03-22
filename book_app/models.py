from django.db import models

class Textbook(models.Model):
    LANGUAGE_CHOICES = [
        ('uz', 'O‘zbek'),
        ('ru', 'Rus'),
        ('en', 'Ingliz'),
    ]

    subject = models.CharField(max_length=255, verbose_name="Fan nomi")
    grade = models.PositiveIntegerField(verbose_name="Sinf")
    file = models.FileField(upload_to='textbooks/', verbose_name="Darslik fayli")
    language = models.CharField(max_length=50, choices=LANGUAGE_CHOICES, verbose_name="Til")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} ({self.grade}-sinf, {self.language})"


class Subject(models.Model):
    """Fanlar modeli"""
    name = models.CharField(max_length=255)  # Fanning nomi
    class_number = models.IntegerField()  # Qaysi sinfga tegishli

    def __str__(self):
        return f"{self.class_number}-sinf: {self.name}"
