UmutDizman.com – Portfolio Website

Personal portfolio website built with Django, deployed on Ubuntu + Nginx + Gunicorn, secured with Let’s Encrypt SSL.


Live: https://umutdizman.com


🚀 Tech Stack
Backend: Django 5.2
Web Server: Nginx
App Server: Gunicorn (systemd socket)
Database: SQLite (MVP)
Static Files: Nginx (collectstatic)
Email: SMTP (Gmail – optional)
Deployment: Ubuntu (DigitalOcean)
SSL: Let’s Encrypt (Certbot)

📁 Project Structure
/var/www/umutdizman/
├── app/
│   ├── venv/                  # Python virtualenv
│   └── umutdizman.com/
│       ├── Portfoy/           # Django project
│       ├── umutdizmancom/     # Main app
│       ├── static/            # Source static files
│       ├── staticfiles/       # collectstatic output
│       ├── templates/
│       ├── locale/
│       ├── manage.py
│       └── .env

⚙️ Environment Variables (.env)
DJANGO_DEBUG=0
DJANGO_SECRET_KEY=your-secret-key
DJANGO_ALLOWED_HOSTS=umutdizman.com,www.umutdizman.com
DJANGO_CSRF_TRUSTED_ORIGINS=https://umutdizman.com,https://www.umutdizman.com

SITE_NAME=Umut Dizman
SITE_URL=https://umutdizman.com

# Email (optional)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=1
EMAIL_HOST_USER=example@gmail.com
EMAIL_HOST_PASSWORD=app-password
DEFAULT_FROM_EMAIL=Umut Dizman <example@gmail.com>
CONTACT_NOTIFY_EMAIL=umutd.zman@gmail.com

# Security (after SSL)
DJANGO_SECURE_SSL_REDIRECT=1
DJANGO_SESSION_COOKIE_SECURE=1
DJANGO_CSRF_COOKIE_SECURE=1


🧪 Local Development
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python manage.py migrate
python manage.py collectstatic
python manage.py runserver

🏗️ Production Setup (Summary)
Gunicorn (systemd + socket)
Socket: /run/gunicorn-umutdizman.sock
User: www-data
Managed by systemd
systemctl status gunicorn-umutdizman

Nginx
Static files served directly
Requests proxied to Gunicorn socket
nginx -t
systemctl reload nginx

SSL
certbot --nginx -d umutdizman.com -d www.umutdizman.com
🧠 Notes / Decisions
SQLite is used intentionally (portfolio-scale traffic).

Email is non-blocking:
form submissions are saved even if SMTP fails.
Systemd socket activation used for clean restarts.
No Docker (intentionally kept simple).

✅ Health Checks
curl -I https://umutdizman.com
curl -I https://umutdizman.com/static/images/logo1.png
systemctl status nginx
systemctl status gunicorn-umutdizman

📬 Contact Form Behavior
Saves submissions to Django Admin
Sends email notification if SMTP is reachable
Never blocks user submission on email failure

🧑‍💻 Author
Umut Dizman
Backend-focused developer building SaaS & freelance products.

📄 License
Private / Personal Project