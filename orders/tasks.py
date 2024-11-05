from celery import shared_task
from django.core.mail import send_mail
from .models import Order
from decouple import config

@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    message = (
        f'Dear {order.first_name},\n\n'
        f'You have successfully placed an order.\n'
        f'Your order ID is {order.id}.'
    )
    mail_sent = send_mail(
        subject,
        message,
        config('EMAIL_HOST_USER'),
        [order.email]
    )
    return mail_sent