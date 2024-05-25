import random
import string

from django.conf import settings
from django.core.mail import send_mail

from coverRencontre.models import Participants, Evenements


def code_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def sending_email(recip_email, evenement: Evenements, message):
    print(settings.EMAIL_HOST_USER)
    subject = f'Inscription au {evenement.name_evenement}'
    message = message
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [recip_email]
    send_mail(subject, message, from_email, recipient_list)
