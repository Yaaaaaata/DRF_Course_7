import os
from celery import shared_task
from datetime import datetime, timedelta

from habits.models import Habit
from habits.services import send_message


@shared_task
def send_habit():
    time_now = datetime.now()
    habits = Habit.objects.all()
    # token = '6855759826:AAFNEV1QcK6LFA9k34AsDFOZINhOYWXI6x8'
    token = os.getenv('TELEGRAM_BOT_TOKEN')

    for habit in habits:
        if habit.time >= time_now - timedelta(minutes=15):
            message = f"Напоминание о привычке {habit.action}" \
                      f"Связанная привычка или награда: {habit.related_habit if habit.related_habit else habit.reward}"
            send_message(token=token, telegram_id=habit.user.telegram_id, message=message)
