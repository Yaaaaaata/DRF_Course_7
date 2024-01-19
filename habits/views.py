from rest_framework import viewsets

from habits.models import Habit
from habits.paginators import HabitPaginator
from habits.serializers import HabitSerializer
from habits.permissions import IsOwnerOrReadOnly, IsPublicHabit


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitPaginator
    permission_classes = [IsOwnerOrReadOnly]


class PublicHabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_public=True)
    permission_classes = [IsPublicHabit]
