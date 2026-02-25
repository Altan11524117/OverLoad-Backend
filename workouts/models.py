from django.db import models
from django.conf import settings

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    target_muscle = models.CharField(max_length=100, help_text="Örn: Göğüs, Sırt, Quadriceps")
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class WorkoutPlan(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='workout_plans')
    title = models.CharField(max_length=150, help_text="Örn: 12 Haftalık Hipertrofi Programı")
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} - {self.user.username}"

class WorkoutDay(models.Model):
    plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE, related_name='days')
    day_name = models.CharField(max_length=50, help_text="Örn: Push Day, Pull Day, Leg Day veya 1. Gün")
    
    def __str__(self):
        return f"{self.plan.title} - {self.day_name}"

class WorkoutExercise(models.Model):
    
    workout_day = models.ForeignKey(WorkoutDay, on_delete=models.CASCADE, related_name='exercises')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.PositiveIntegerField(default=3)
    reps = models.CharField(max_length=50, help_text="Örn: 8-12, 5x5 veya Tükeniş")

    def __str__(self):
        return f"{self.exercise.name} ({self.sets} Set) - {self.workout_day.day_name}"