from django.urls import path
from .views import GenerateWorkoutView, WorkoutPlanListView

urlpatterns = [
    path('generate/', GenerateWorkoutView.as_view(), name='generate_workout'),
    path('plans/', WorkoutPlanListView.as_view(), name='list_plans'), 
]