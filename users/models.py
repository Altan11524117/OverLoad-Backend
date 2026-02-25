from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    
    GOAL_CHOICES = [
        ('BULK', 'Bulking (Kütle Kazanımı)'),
        ('CUT', 'Cutting (Yağ Yakımı)'),
        ('MAINTAIN', 'Koruma'),
    ]

    EXPERIENCE_CHOICES = [
        ('BEGINNER', 'Başlangıç'),
        ('INTERMEDIATE', 'Orta Seviye'),
        ('ADVANCED', 'İleri Seviye'),
    ]

    height = models.FloatField(null=True, blank=True, help_text="Santimetre cinsinden boy")
    weight = models.FloatField(null=True, blank=True, help_text="Kilogram cinsinden ağırlık")
    fitness_goal = models.CharField(max_length=20, choices=GOAL_CHOICES, default='BULK')
    experience_level = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='BEGINNER')

    def __str__(self):
        return self.username