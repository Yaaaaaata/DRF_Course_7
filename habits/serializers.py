from rest_framework import serializers

from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'

    def validate(self, data):
        if data.get('related_habit') and data.get('reward'):
            raise serializers.ValidationError("Связанная привычка и награда не могут быть выбраны одновременно.")
        if data.get('time_to_complete') > 120:
            raise serializers.ValidationError("Время выполнения не может превышать 120 секунд..")
        if data.get('related_habit') and not data['related_habit'].is_pleasant_habit:
            raise serializers.ValidationError("Сопутствующая привычка должна быть приятной привычкой.")
        if data.get('is_pleasant_habit') and (data.get('reward') or data.get('related_habit')):
            raise serializers.ValidationError("Приятная привычка не может иметь награды или связанной с ней привычки.")
        if data.get('frequency') < 7:
            raise serializers.ValidationError("Периодичность не может быть меньше 7 дней.")
        return data
