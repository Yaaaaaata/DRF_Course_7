from django.urls import path, include
from rest_framework.routers import DefaultRouter

from habits.apps import HabitsConfig
from habits.views import HabitViewSet, PublicHabitViewSet

app_name = HabitsConfig.name

router = DefaultRouter()
router.register(r'habits', HabitViewSet, basename='habits')

urlpatterns = [
    path('', include(router.urls)),
    path('habits/', HabitViewSet.as_view({'post': 'create'}), name='create_habit'),
    path('public_habits/', PublicHabitViewSet.as_view({'get': 'list'}), name='public_habits'),
    path('habits/<int:pk>/', HabitViewSet.as_view({'patch': 'update', 'delete': 'destroy'}), name='habit_detail'),
] + router.urls
