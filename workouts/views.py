from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .services import generate_workout_plan_for_user
from rest_framework.generics import ListAPIView
from .models import WorkoutPlan
from .serializers import WorkoutPlanSerializer

class GenerateWorkoutView(APIView):
    
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        
        
        if not user.height or not user.weight:
            return Response({"error": "Boy ve kilo bilgileriniz eksik. Lütfen profilinizi güncelleyin."}, status=400)

        try:
           
            plan = generate_workout_plan_for_user(user)
            return Response({
                "message": "Yapay zeka programınızı başarıyla oluşturdu!",
                "plan_id": plan.id,
                "plan_title": plan.title
            }, status=201)
            
        except Exception as e:
            return Response({"error": f"Program oluşturulurken bir hata oluştu: {str(e)}"}, status=500)


class WorkoutPlanListView(ListAPIView):
    serializer_class = WorkoutPlanSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        
        return WorkoutPlan.objects.filter(user=self.request.user).order_by('-created_at')