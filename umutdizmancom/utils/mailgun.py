# umutdizmancom/utils/mailgun.py
import os
import requests

def send_mailgun(*, subject: str, text: str, to_emails: list[str], from_email: str, html: str | None = None, reply_to: str | None = None) -> dict:
    api_key = os.environ["MAILGUN_API_KEY"]
    domain = os.environ["MAILGUN_DOMAIN"]
    base = os.environ.get("MAILGUN_API_BASE", "https://api.eu.mailgun.net/v3").rstrip("/")
    url = f"{base}/{domain}/messages"

    data = {
        "from": from_email,
        "to": to_emails,
        "subject": subject,
        "text": text,
    }
    if html:
        data["html"] = html
    if reply_to:
        data["h:Reply-To"] = reply_to

    r = requests.post(url, auth=("api", api_key), data=data, timeout=20)
    r.raise_for_status()
    return r.json()
