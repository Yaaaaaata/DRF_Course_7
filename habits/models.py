from django.db import models

from config import settings

NULLABLE = {'null': True, 'blank': True}


class Habit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    place = models.CharField(max_length=100, verbose_name='Место', **NULLABLE)
    time = models.TimeField(verbose_name='Время', **NULLABLE)
    action = models.CharField(max_length=100, verbose_name='Действие')
    is_pleasant_habit = models.BooleanField(default=False, verbose_name='Признак приятной привычки')
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='Связанная привычка', **NULLABLE)
    frequency = models.PositiveIntegerField(default=1, verbose_name='Периодичность', **NULLABLE)
    reward = models.CharField(max_length=100, verbose_name='Вознаграждение', **NULLABLE)
    time_to_complete = models.PositiveIntegerField(default=120, verbose_name='Время на выполнение', **NULLABLE)
    is_public = models.BooleanField(default=False, verbose_name='Признак публичности')

    def __str__(self):
        return f'{self.action} - {self.time} - {self.place}'

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
