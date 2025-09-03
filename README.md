# django-chat-site

Real-time chat application built with Django, Django Channels, and WebSockets

---

## 🚀 Introduction

Welcome to **django-chat-site**, a simple but powerful real-time chat app where users can create accounts, join chat rooms, and exchange messages instantly. Built on Django’s robust framework and leveraging WebSockets via Django Channels, this project demonstrates how to bring live interactivity to your web applications.

---

## 🌟 Features

* **User Authentication**
  Sign up, log in, and log out securely with Django’s built-in auth system.

* **Chat Rooms**
  Create or join named chat rooms to discuss topics with others in real time.

* **Live Messaging**
  Instantly broadcast messages to all participants in a room using WebSockets.

* **Responsive UI**
  Mobile-friendly design so you can chat on any device.

* **Scalable**
  Ready to extend with Redis or other channel layers for production use.

---

## 📦 Tech Stack

* **Python
* **Django
* **Django Channels
* **Redis**
* **HTML5 / CSS3 / JavaScript**
* **Bootstrap 5**

---

## 🔧 Prerequisites

* Python 3.8 or newer
* pip (Python package installer)
* (Optional) Redis server for channel layer in production

---

## ⚙️ Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/django-chat-site.git
   cd django-chat-site
   ```

2. **Create and activate a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## 🔐 Configuration

1. **Environment variables**
   Create a `.env` file in the project root (or set environment variables directly):

   ```ini
   SECRET_KEY=your_django_secret_key
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   REDIS_URL=redis://127.0.0.1:6379/0   # (Optional for Channels)
   ```

2. **Database migration**

   ```bash
   python manage.py migrate
   ```

3. **Create a superuser**

   ```bash
   python manage.py createsuperuser
   ```

---

## ▶️ Running the App

You can run the development server with or without Redis:

* **Without Redis (in-memory channel layer)**

  ```bash
  python manage.py runserver
  ```

* **With Redis (recommended for production-like testing)**
  Make sure your Redis server is running, then:

  ```bash
  python manage.py runserver
  ```

Visit `http://127.0.0.1:8000/` in your browser, sign up or log in, and start chatting!

---

## 📝 Usage

1. Sign up for a new account or log in with existing credentials.
2. Create a new chat room by entering a room name and clicking **“Create”**.
3. Click on any room name to join the conversation.
4. Type your message in the input box and press **Enter** or click **Send**.
5. Watch messages appear in real time as other users join and chat!

---

## 🤝 Contributing

Contributions are welcome! Here’s how to get started:

1. Fork this repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m "Add awesome feature"`)
4. Push to your branch (`git push origin feature/YourFeature`)
5. Open a pull request outlining your changes
