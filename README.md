# UmutDizman.com — Portfolio & Case Study Platform

Personal portfolio and case study platform built with **Django**, designed to showcase
product-focused projects, architectural decisions and an end-to-end delivery approach
from development to production.

🌍 **Live:** https://umutdizman.com

---

## 🛠️ Technical Overview

- **Backend:** Django  
- **Web Server:** Nginx  
- **App Server:** Gunicorn  
- **Database:** SQLite (MVP)   
- **Deployment:** Ubuntu (DigitalOcean)  
- **SSL:** Let’s Encrypt

---

## 🧠 Product & Ownership Focus

The project intentionally avoids unnecessary complexity and favors
clear, understandable solutions over over-engineering.

Key decisions:
- Clear separation of concerns (views, templates, static assets)
- Production-ready deployment with proper process management
- Secure configuration using environment variables
- SEO-friendly structure and performance-conscious setup

The goal was to treat even a personal website like a real product:
deployable, maintainable and owned end-to-end.

> Included for deployment clarity and operational context.

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
