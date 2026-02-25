# 🏋️‍♂️ Overload - Yapay Zeka Destekli Fitness API

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Django](https://img.shields.io/badge/Django-6.0-092E20?logo=django)
![Django REST Framework](https://img.shields.io/badge/DRF-Red?logo=django)
![Google Gemini](https://img.shields.io/badge/AI-Google_Gemini_2.5-8E75B2?logo=google)
![JWT](https://img.shields.io/badge/Security-JWT-black?logo=jsonwebtokens)

**Overload**, kullanıcının fiziksel verilerini ve Google'ın Üretken Yapay Zekasını (Gemini) kullanarak kişiye özel, bilimsel tabanlı antrenman programları oluşturan modern bir backend API mimarisidir. 

Bu proje, güvenli veri akışı, harici API entegrasyonu, dinamik prompt mühendisliği ve temiz veritabanı mimarisine odaklanan **"Saf Backend"** (Pure Backend) anlayışıyla geliştirilmiştir.

---

## 🚀 Öne Çıkan Mimari Özellikler

* **🧠 Gelişmiş Yapay Zeka Entegrasyonu:** Kullanıcının Boy, Kilo, Deneyim Seviyesi ve Hedefleri üzerinden spesifik promptlar oluşturur. Gemini AI çıktılarını `application/json` formatında parse ederek ilişkisel veritabanına kaydeder.
* **🔐 Güvenli Kimlik Doğrulama:** Stateless ve güvenli API iletişimi için **JWT (JSON Web Tokens)** ile entegre edilmiş bir Custom User Model kullanılmıştır.
* **📐 Dinamik Antrenman Mantığı:** Kullanıcının deneyim seviyesine göre (Başlangıç seviyesi için Full-Body, ileri seviye için PPL gibi) antrenman stillerini otomatik olarak değiştirir.
* **📖 Otomatik API Dokümantasyonu:** `drf-spectacular` entegrasyonu ile oluşturulan etkileşimli **Swagger UI**, backend uç noktalarının kolayca test edilmesini sağlar.
* **🗄️ İlişkisel Veritabanı Şeması:** Kullanıcılar, Antrenman Planları, Günler ve Egzersizler arasındaki ilişkileri yöneten titizlikle tasarlanmış SQLite şeması.

---

## 🛠️ Teknoloji Yığını

* **Backend Framework:** Django 6.0.2, Django REST Framework (DRF)
* **Yapay Zeka:** Google Generative AI SDK (Gemini 2.5 Flash)
* **Kimlik Doğrulama:** `djangorestframework-simplejwt`
* **API Dokümantasyonu:** Swagger UI (`drf-spectacular`)
* **Güvenlik:** `python-dotenv` (SECRET_KEY ve API anahtarlarının korunması için)

---

## ⚙️ Kurulum ve Çalıştırma

Lokal ortamınızda projeyi ayağa kaldırmak için şu adımları izleyin:

**1. Depoyu klonlayın:**
```bash
git clone [https://github.com/KULLANICI_ADIN/overload-api.git](https://github.com/KULLANICI_ADIN/overload-api.git)
cd overload-api

python -m venv venv
# Windows için:
venv\Scripts\activate

pip install -r requirements.txt

DJANGO_SECRET_KEY=senin_django_secret_keyin
GEMINI_API_KEY=senin_gemini_api_keyin

python manage.py migrate
python manage.py createsuperuser  
python manage.py runserver

```
📡 API Uç Noktaları ve Test Etme
1. Etkileşimli Swagger UI
API'yi keşfetmenin en kolay yolu Swagger arayüzüdür. Sunucu çalışırken şu adrese gidin:
👉 http://127.0.0.1:8000/api/docs/

2. Postman Koleksiyonu
Ana dizinde bulunan overLoad.postman_collection.json dosyasını Postman'e "Import" ederek tüm hazır istekleri görebilirsiniz.

Temel Endpointler:
POST /auth/register/ - Kullanıcı kaydı ve fiziksel metriklerin girişi.

POST /auth/login/ - JWT Access ve Refresh token alma.

POST /workouts/generate/ - Gemini AI'yı tetikleyerek kişiye özel plan oluşturma.

GET /workouts/plans/ - Kullanıcının geçmiş planlarını listeleme.

🔗 LinkedIn: [https://www.linkedin.com/in/altan-ayd%C4%B1n/]

🐙 GitHub: [https://github.com/Altan11524117]
