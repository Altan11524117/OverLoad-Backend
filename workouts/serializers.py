from rest_framework import serializers
from .models import WorkoutPlan, WorkoutDay, WorkoutExercise

class WorkoutExerciseSerializer(serializers.ModelSerializer):
   
    exercise_name = serializers.CharField(source='exercise.name', read_only=True)
    target_muscle = serializers.CharField(source='exercise.target_muscle', read_only=True)

    class Meta:
        model = WorkoutExercise
        fields = ['exercise_name', 'target_muscle', 'sets', 'reps']

class WorkoutDaySerializer(serializers.ModelSerializer):
    
    exercises = WorkoutExerciseSerializer(many=True, read_only=True)

    class Meta:
        model = WorkoutDay
        fields = ['day_name', 'exercises']

class WorkoutPlanSerializer(serializers.ModelSerializer):
    
    days = WorkoutDaySerializer(many=True, read_only=True)

    class Meta:
        model = WorkoutPlan
        fields = ['id', 'title', 'created_at', 'is_active', 'days']