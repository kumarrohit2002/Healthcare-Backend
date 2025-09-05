# mappings/urls.py

from django.urls import path
from .views import MappingListCreateView, MappingRetrieveDeleteView

urlpatterns = [
    path('', MappingListCreateView.as_view(), name='mappings-list-create'),
    path('<int:pk>/', MappingRetrieveDeleteView.as_view(), name='mappings-rd'),
]
