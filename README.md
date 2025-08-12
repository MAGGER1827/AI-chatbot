# AI-Chatbot

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2-green.svg)](https://www.djangoproject.com/)
[![Keras](https://img.shields.io/badge/Keras-2.12-red.svg)](https://keras.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Django-powered AI chatbot trained on a custom intents dataset, delivering precise and immediate responses with a sleek, responsive Bootstrap UI.

---

## Features
- 🧠 Deep learning–based intent recognition using **Keras** & **NLTK**
- 💬 Instant and context-aware responses
- 🎨 Clean, fully responsive frontend (Bootstrap & Font Awesome)
- 🔒 Secure form handling with CSRF protection
- ⚡ Easily customizable intents and responses

---

## Tech Stack
- **Backend:** Django, Keras, NLTK
- **Frontend:** HTML5, CSS3, Bootstrap, Font Awesome
- **Assets:** Trained model, intents JSON, pickled word lists, and classes

---

## Setup Guide

1. **Clone the repository**  
   ```bash
   git clone https://github.com/malavika-suresh/AI-chatbot.git
   cd AI-chatbot
   ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Place model files** in the correct path (update paths in `views.py` if necessary):  
   - `model_new.h5`  
   - `new_intent.json`  
   - `words.pkl`  
   - `classes.pkl`  

4. **Run migrations** (if applicable)  
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**  
   ```bash
   python manage.py runserver
   ```

---

## Project Structure
```

AI-chatbot/
├── chat/
│ ├── pycache/
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── chatbot/
│ ├── pycache/
│ ├── migrations/
│ ├── templates/webbot/
│ │ └── index.html
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
├── files/
│ ├── classes.pkl
│ ├── model_new.h5
│ ├── new_intent.json
│ └── words.pkl
├── db.sqlite3
└── manage.py
```


