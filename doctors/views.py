from rest_framework import generics, permissions
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorListCreateView(generics.ListCreateAPIView):
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Doctor.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DoctorRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Doctor.objects.all()
