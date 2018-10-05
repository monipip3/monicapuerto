import logging
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.core.mail import send_mail
from collection.forms import ContactForm


logger = logging.getLogger(__name__)


HTTP_POST = "POST"
HTTP_400_BAD_REQUEST = 400
HTTP_200_OK = 200
HTTP_500_INTERNAL_SERVER_ERROR = 500


def _send_email(contact_form):
    """
    Send an email about the data
    captured in the contact form
    :param contact_form: ContactForm instance
    :return: None
    :raise: SMTPException
    """
    # TODO: set up for sending an email through heroku
    # the example here is using django send_mail, which expects an smtp server running on heroku
    # https://docs.djangoproject.com/en/2.1/topics/email/#module-django.core.mail

    # or you could do something like this:
    # https://medium.com/@MicroPyramid/sending-emails-using-sendgrid-on-heroku-for-a-django-app-ab856a63fd1

    # build message
    name = contact_form.cleaned_data['name']
    email = contact_form.cleaned_data['email']
    phone = contact_form.cleaned_data['phone']
    message = contact_form.cleaned_data['message']

    to_email = settings.CONTACT_TO_EMAIL
    from_email = settings.CONTACT_REPLY_EMAIL
    email_subject = "Website Contact Form: {0}".format(name)
    email_body = ("You have received a new message from your website contact form.\n\n"
                  "Here are the details:\n\nName: {0}\n\nEmail: {1}\n\n"
                  "Phone: {2}\n\nMessage:\n{3}"
                  .format(name, email, phone, message))
    logger.debug(email_body)

    # send message
    send_mail(email_subject, email_body,
              from_email, [to_email],
              fail_silently=False,
              )


def index(request):
    return render(request, 'index.html')


def contact_form(request):
    """
    View for handling ajax post requests from the contact form.
    This view will send an email and return an HTTP status
    for the ajax caller.
    :return: JsonResponse with status
    """
    status = HTTP_400_BAD_REQUEST
    if request.method == HTTP_POST and request.is_ajax():
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                _send_email(form)
                status = HTTP_200_OK
            except Exception as e:
                logger.error("Unable to send contact form email. Error: %s", e)
                status = HTTP_500_INTERNAL_SERVER_ERROR

    return JsonResponse({"response": status}, status=status)
