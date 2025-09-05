from rest_framework import generics, permissions
from .models import Patient
from .serializers import PatientSerializer

class PatientListCreateView(generics.ListCreateAPIView):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Patient.objects.all()  # Or filter by user if needed

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PatientRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Patient.objects.all()
