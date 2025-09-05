from django.urls import path
from .views import DoctorListCreateView, DoctorRetrieveUpdateDeleteView

urlpatterns = [
    path('', DoctorListCreateView.as_view(), name='doctors-list-create'),
    path('<int:pk>/', DoctorRetrieveUpdateDeleteView.as_view(), name='doctors-rud'),
]
