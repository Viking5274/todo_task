from celery import shared_task

from django.core.mail import send_mail


@shared_task
def send_email_task(gmails, title):
    print(gmails)
    message = "Вам была поставлена задача {}".format(title)
    send_mail(
        "Задача",
        message,
        'from@example.com',
        gmails,
    )

    return None
