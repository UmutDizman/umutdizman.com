# umutdizmancom/tasks.py
import logging
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.utils.translation import gettext as _

logger = logging.getLogger(__name__)

def _abs(url_path: str) -> str:
    """
    '/static/..' gibi path'i SITE_URL ile absolute URL'e çevirir.
    Email client'lar için şart.
    """
    base = getattr(settings, "SITE_URL", "").rstrip("/")
    if url_path.startswith("http://") or url_path.startswith("https://"):
        return url_path
    if not url_path.startswith("/"):
        url_path = "/" + url_path
    return f"{base}{url_path}"

def _wrap_email_html(*, title, intro, lines, cta_text=None, cta_url=None, footer_note=None):
    """
    Client-safe HTML email (inline CSS).
    Header: 640x150 image (logo1.png) -> senin yaptığın tasarım.
    """
    brand = getattr(settings, "SITE_NAME", "Umut Dizman")

    header_src = _abs(getattr(settings, "EMAIL_HEADER_IMAGE_PATH", "/static/images/logo1.png"))

    items_html = "".join([f"<li style='margin:0 0 10px 0;'>{line}</li>" for line in lines])

    cta_html = ""
    if cta_text and cta_url:
        cta_html = f"""
        <div style="margin-top:20px;text-align:center;">
          <a href="{cta_url}"
             style="display:inline-block;background:#2563eb;color:#ffffff;text-decoration:none;
                    padding:14px 18px;border-radius:12px;font-weight:700;">
            {cta_text}
          </a>
        </div>
        """

    footer_html = f"""
      <p style="margin:20px 0 0 0;color:#6b7280;font-size:13px;line-height:1.55;text-align:center;">
        {footer_note or _("If you didn’t request this, you can ignore this email.")}
      </p>
    """

    return f"""\
<!doctype html>
<html>
  <body style="margin:0;background:#f6f7fb;padding:24px;font-family:Inter,system-ui,-apple-system,Segoe UI,Roboto,Arial;">
    <div style="max-width:640px;margin:0 auto;">

      <!-- HEADER IMAGE -->
      <div style="background:#ffffff;border-radius:16px 16px 0 0;overflow:hidden;
                  border:1px solid rgba(17,24,39,.08);border-bottom:none;">
        <img src="{header_src}" width="640" height="150" alt="{brand}"
             style="display:block;width:100%;height:auto;line-height:0;border:0;outline:none;text-decoration:none;" />
      </div>

      <!-- CARD BODY -->
      <div style="background:#ffffff;border:1px solid rgba(17,24,39,.08);border-top:none;
                  border-radius:0 0 16px 16px;padding:22px 20px 20px;
                  box-shadow:0 12px 30px rgba(15,23,42,.06);">

        <h1 style="margin:0 0 10px 0;font-size:22px;line-height:1.25;color:#111827;text-align:center;">
          {title}
        </h1>

        <p style="margin:0 0 16px 0;color:#374151;line-height:1.65;text-align:center;">
          {intro}
        </p>

        <div style="max-width:520px;margin:0 auto;">
          <ul style="margin:0;padding-left:18px;color:#374151;line-height:1.7;">
            {items_html}
          </ul>
        </div>

        {cta_html}
        {footer_html}
      </div>

      <p style="margin:14px 0 0 0;color:#9ca3af;font-size:12px;text-align:center;">
        © {brand}
      </p>
    </div>
  </body>
</html>
"""

def send_inquiry_emails(inquiry):
    # --- Admin mail ---
    try:
        admin_subject = f"[New Inquiry] {inquiry.name} — {inquiry.package}"

        admin_text = (
            "New inquiry received.\n\n"
            f"Name: {inquiry.name}\n"
            f"Email: {inquiry.email}\n"
            f"Phone: {inquiry.phone or '-'}\n"
            f"Package: {inquiry.get_package_display()}\n\n"
            f"Message:\n{inquiry.message}\n\n"
            f"Admin: {_abs('/admin/')}\n"
        )

        admin_html = _wrap_email_html(
            title=_("New project inquiry"),
            intro=_("You received a new inquiry. Summary:"),
            lines=[
                f"<strong>{_('Name')}:</strong> {inquiry.name}",
                f"<strong>{_('Email')}:</strong> {inquiry.email}",
                f"<strong>{_('Phone')}:</strong> {inquiry.phone or '-'}",
                f"<strong>{_('Package')}:</strong> {inquiry.get_package_display()}",
                f"<strong>{_('Message')}:</strong> {inquiry.message}",
            ],
            cta_text=_("Open Admin"),
            cta_url=_abs("/admin/"),
            footer_note=_("Tip: reply quickly to improve conversion."),
        )

        msg = EmailMultiAlternatives(
            subject=admin_subject,
            body=admin_text,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.CONTACT_NOTIFY_EMAIL],
            reply_to=[inquiry.email],
        )
        msg.attach_alternative(admin_html, "text/html")
        msg.send(fail_silently=False)
    except Exception:
        logger.exception("Admin notification email failed")

    # --- User mail ---
    try:
        user_subject = _("Got it — I’ll get back to you shortly")

        user_text = (
            _("Thanks for reaching out. I’ve received your message and I’ll reply within 24 hours.\n\n")
            + f"{_('Package')}: {inquiry.get_package_display()}\n"
            + f"{_('Your message')}: {inquiry.message}\n"
        )

        user_html = _wrap_email_html(
            title=_("Message received ✅"),
            intro=_("Thanks for reaching out. I’ll review your message and reply within 24 hours."),
            lines=[
                f"<strong>{_('Package')}:</strong> {inquiry.get_package_display()}",
                f"<strong>{_('Next step')}:</strong> {_('I’ll respond with timeline + questions (if needed).')}",
            ],
            cta_text=_("View Services"),
            cta_url=_abs("/services/"),
            footer_note=_("If you have extra details, reply to this email."),
        )

        msg = EmailMultiAlternatives(
            subject=user_subject,
            body=user_text,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[inquiry.email],
            reply_to=[settings.CONTACT_NOTIFY_EMAIL],
        )
        msg.attach_alternative(user_html, "text/html")
        msg.send(fail_silently=False)
    except Exception:
        logger.exception("User autoreply email failed")
