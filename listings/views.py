# views.py
from rest_framework import viewsets
from .models import Discipline, Candidat, Vote
from .serializers import DisciplineSerializer, CandidatSerializer, VoteSerializer

class DisciplineViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer

class CandidatViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Candidat.objects.all()
    serializer_class = CandidatSerializer

class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

    # Customize the update method to handle payment confirmation
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        payment_confirmed = request.data.get("payment_confirmed", instance.payment_confirmed)
        instance.payment_confirmed = payment_confirmed
        instance.save()
        return super().update(request, *args, **kwargs)
