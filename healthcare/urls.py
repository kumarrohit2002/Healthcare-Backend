from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Home view with all API endpoints
from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "message": "Welcome to the Healthcare API!",
        "endpoints": {
            "JWT Authentication": {
                "obtain_token (POST)": "/api/token/",
                "refresh_token (POST)": "/api/token/refresh/"
            },
            "Accounts": {
                "register (POST)": "/api/accounts/register/",
                "login (POST)": "/api/accounts/login/"
            },
            "Patients": {
                "add patients (POST)": "/api/patients/",
                "retrieve_update_delete (GET, PUT, DELETE)": "/api/patients/<id>/"
            },
            "Doctors": {
                "add doctor (POST)": "/api/doctors/",
                "retrieve_update_delete (GET, PUT, DELETE)": "/api/doctors/<id>/"
            },
            "Mappings (Patient-Doctor)": {
                "assign doctor to patient (POST)": "/api/mappings/",
                "get all mappings (GET)": "/api/mappings/",
                "get mappings by patient (GET)": "/api/mappings/<patient_id>/",
                "remove mapping (DELETE)": "/api/mappings/<id>/"
            }
        }
    })




urlpatterns = [
    path('', home, name='home'),  # Root path
    path('admin/', admin.site.urls),

    # JWT Authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # App routes
    path('api/accounts/', include('accounts.urls')),
    path('api/patients/', include('patients.urls')),
    path('api/doctors/', include('doctors.urls')),
    path('api/mappings/', include('mappings.urls')),
]


