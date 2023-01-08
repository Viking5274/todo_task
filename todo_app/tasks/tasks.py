from celery import shared_task

from django.core.mail import send_mail


@shared_task
def send_email_task(gmails, title, status):
    print(gmails)
    message = "Обновлен статус задачи: {} для задачи {}".format(status, title)
    send_mail(
        "Задача",
        message,
        'from@example.com',
        gmails,
    )

    return None
