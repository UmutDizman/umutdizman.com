# UmutDizman.com — Portfolio Website

Personal portfolio website built with **Django**, deployed on **Ubuntu + Nginx + Gunicorn**, secured with **Let’s Encrypt SSL**.

🌍 **Live:** https://umutdizman.com

---

## 🚀 Tech Stack

- **Backend:** Django 5.2  
- **Web Server:** Nginx  
- **App Server:** Gunicorn (systemd socket)  
- **Database:** SQLite (MVP)  
- **Static Files:** Nginx (`collectstatic`)  
- **Email:** SMTP (Gmail – optional)  
- **Deployment:** Ubuntu (DigitalOcean)  
- **SSL:** Let’s Encrypt (Certbot)

---

## 📁 Project Structure

```text
/var/www/umutdizman/
├── app/
│   ├── venv/                  # Python virtual environment
│   └── umutdizman.com/
│       ├── Portfoy/           # Django project
│       ├── umutdizmancom/     # Main app
│       ├── static/            # Source static files
│       ├── staticfiles/       # collectstatic output
│       ├── templates/
│       ├── locale/
│       ├── manage.py
│       └── .env
