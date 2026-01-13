# umutdizmancom/tasks.py
import logging
from django.conf import settings
from django.core.mail import send_mail
from django.utils.translation import gettext as _

logger = logging.getLogger(__name__)

def send_inquiry_emails(inquiry):
    """Send admin + user emails. Runs in background thread."""
    try:
        admin_subject = f"[New Inquiry] {inquiry.name} — {inquiry.package}"
        admin_body = (
            f"Name: {inquiry.name}\n"
            f"Email: {inquiry.email}\n"
            f"Phone: {inquiry.phone or '-'}\n"
            f"Package: {inquiry.get_package_display()}\n\n"
            f"Message:\n{inquiry.message}\n\n"
            f"Admin: {settings.SITE_URL}/admin/"
        )

        send_mail(
            subject=admin_subject,
            message=admin_body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.CONTACT_NOTIFY_EMAIL],
            fail_silently=False,
        )
    except Exception:
        logger.exception("Admin notification email failed")

    try:
        user_subject = _("Got it — I’ll get back to you shortly")
        user_body = _(
            "Thanks for reaching out. I’ve received your message and I’ll reply within 24 hours.\n\n"
            "Summary:\n"
        ) + f"- Package: {inquiry.get_package_display()}\n- Message: {inquiry.message}\n"

        send_mail(
            subject=user_subject,
            message=user_body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[inquiry.email],
            fail_silently=False,
        )
    except Exception:
        logger.exception("User autoreply email failed")
