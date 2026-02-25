import json
import google.generativeai as genai
from .models import WorkoutPlan, WorkoutDay, WorkoutExercise, Exercise
import os
from dotenv import load_dotenv

load_dotenv() 

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

def generate_workout_plan_for_user(user):
  
    prompt = f"""
    Sen elit seviye bir vücut geliştirme antrenörü ve spor bilimcisisin. 
    Amacın, aşağıdaki kullanıcının fiziksel verilerine ve hedeflerine en uygun, tamamen bilimsel temelli ve modern bir antrenman programı oluşturmak.

    KULLANICI PROFİLİ:
    - Boy: {user.height} cm
    - Kilo: {user.weight} kg
    - Hedef: {user.fitness_goal}
    - Deneyim Seviyesi: {user.experience_level}

    GÖREV KURALLARI (ÇOK ÖNEMLİ):
    1. Kademeli Sistem: EĞER Deneyim Seviyesi "BEGINNER" (Başlangıç) ise kesinlikle haftada 3 günlük "Full Body" veya "5x5" temel kuvvet programı yaz. EĞER Deneyim Seviyesi "INTERMEDIATE" (Orta) veya "ADVANCED" (İleri) ise "Push/Pull/Legs (PPL)" veya "Upper/Lower" gibi 4-5 günlük bölgesel (split) programlar yaz.
    2. Yoğunluk Belirt (RIR/Failure): Set ve tekrarları yazarken sıradan rakamlar kullanma. Profesyonel programlardaki gibi hipertrofi odaklı RIR (Reps in Reserve) veya Failure (Tükeniş) komutlarını 'reps' alanının içine yaz. (Örn: "6-8 (RIR 1)", "10-12 (Failure)").
    3. Hedef Kas: "Genel" gibi yuvarlak ifadeler kullanma, "Üst Göğüs", "Yan Omuz", "Latissimus Dorsi" gibi spesifik kas gruplarını yaz.
    4. SADECE aşağıdaki JSON formatında çıktı ver. Başında veya sonunda markdown (```json) veya ekstra bir açıklama KESİNLİKLE OLMASIN.

    BEKLENEN JSON FORMATI:
    {{
        "title": "Programın Adı (Örn: İleri Seviye PPL Hipertrofi Programı)",
        "days": [
            {{
                "day_name": "1. Gün: Push (Göğüs, Omuz, Arka Kol)",
                "exercises": [
                    {{"name": "Incline Dumbbell Press", "sets": 4, "reps": "6-8 (RIR 1)", "target_muscle": "Üst Göğüs"}},
                    {{"name": "Lateral Raise", "sets": 3, "reps": "12-15 (Failure)", "target_muscle": "Yan Omuz"}},
                    {{"name": "Triceps Pushdown", "sets": 3, "reps": "10-12", "target_muscle": "Arka Kol"}}
                ]
            }}
        ]
    }}
    """

    model = genai.GenerativeModel("gemini-2.5-flash")
    
    response = model.generate_content(
        prompt,
        generation_config=genai.GenerationConfig(
            response_mime_type="application/json",
            temperature=0.7,
        )
    )

 
    raw_content = response.text
    data = json.loads(raw_content)

  
    plan = WorkoutPlan.objects.create(
        user=user,
        title=data.get('title', 'Yapay Zeka Antrenman Programı (Gemini)')
    )

    for day_data in data.get('days', []):
        day = WorkoutDay.objects.create(
            plan=plan,
            day_name=day_data['day_name']
        )

        for ex_data in day_data.get('exercises', []):
            exercise_obj, created = Exercise.objects.get_or_create(
                name=ex_data['name'],
                defaults={'target_muscle': ex_data.get('target_muscle', 'Genel')}
            )

            WorkoutExercise.objects.create(
                workout_day=day,
                exercise=exercise_obj,
                sets=ex_data.get('sets', 3),
                reps=ex_data.get('reps', '10')
            )

    return plan