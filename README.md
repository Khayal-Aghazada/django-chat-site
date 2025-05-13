# django-chat-site

Real-time chat application built with Django, Django Channels, and WebSockets

---

## 🚀 Introduction

Welcome to **django-chat-site**, a simple but powerful real-time chat app where users can create accounts, join chat rooms, and exchange messages instantly. Built on Django’s robust framework and leveraging WebSockets via Django Channels, this project demonstrates how to bring live interactivity to your web applications.

---

## 🌟 Features

- **User Authentication**  
  Sign up, log in, and log out securely with Django’s built-in auth system.

- **Chat Rooms**  
  Create or join named chat rooms to discuss topics with others in real time.

- **Live Messaging**  
  Instantly broadcast messages to all participants in a room using WebSockets.

- **Responsive UI**  
  Mobile-friendly design so you can chat on any device.

- **Scalable**  
  Ready to extend with Redis or other channel layers for production use.

---

## 📦 Tech Stack

- **Python 3.x**  
- **Django 4.x**  
- **Django Channels 4.x**  
- **Redis** (optional for production channel layer)  
- **HTML5 / CSS3 / JavaScript**  
- **Bootstrap 5** (for styling)

---

## 🔧 Prerequisites

- Python 3.8 or newer  
- pip (Python package installer)  
- (Optional) Redis server for channel layer in production  

---

## ⚙️ Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/django-chat-site.git
   cd django-chat-site
2. Create and activate a virtual environment

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
🔐 Configuration
Environment variables
Create a .env file in the project root (or set environment variables directly):

ini
Copy
Edit
SECRET_KEY=your_django_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
REDIS_URL=redis://127.0.0.1:6379/0   # (Optional for Channels)
Database migration

bash
Copy
Edit
python manage.py migrate
Create a superuser

bash
Copy
Edit
python manage.py createsuperuser
▶️ Running the App
You can run the development server with or without Redis:

Without Redis (in-memory channel layer)

bash
Copy
Edit
python manage.py runserver
With Redis (recommended for production-like testing)
Make sure your Redis server is running, then:

bash
Copy
Edit
python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser, sign up or log in, and start chatting!

📝 Usage
Sign up for a new account or log in with existing credentials.

Create a new chat room by entering a room name and clicking “Create”.

Click on any room name to join the conversation.

Type your message in the input box and press Enter or click Send.

Watch messages appear in real time as other users join and chat!

🤝 Contributing
Contributions are welcome! Here’s how to get started:

Fork this repository

Create a feature branch (git checkout -b feature/YourFeature)

Commit your changes (git commit -m "Add awesome feature")

Push to your branch (git push origin feature/YourFeature)

Open a pull request outlining your changes
