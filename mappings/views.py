from rest_framework import generics, permissions
from .models import Mapping
from .serializers import MappingSerializer

class MappingListCreateView(generics.ListCreateAPIView):
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Mapping.objects.all()


class MappingRetrieveDeleteView(generics.RetrieveDestroyAPIView):
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Mapping.objects.all()
