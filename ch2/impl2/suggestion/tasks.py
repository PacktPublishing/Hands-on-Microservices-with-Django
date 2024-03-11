from time import sleep
from django.core.mail import send_mail
from celery import shared_task


@shared_task()
def send_email_task(name, email_address, suggestion):
    sleep(10)
    send_mail(
        "Your suggestion",
        f"We'll include your suggestion – {suggestion} – into our improvement process.\n\nThanks for your contribution!",
        "quality@xyz.com",
        [email_address],
        fail_silently=False,
    )
