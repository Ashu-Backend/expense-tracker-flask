# 💸 Expense Tracker (Flask)

🚀 A simple and efficient **Expense Tracker Web App** built using **Flask + MySQL** to manage daily expenses with user authentication.

---

## ✨ Features

🔐 User Authentication

* Register new users
* Secure login system
* Logout functionality

💰 Expense Management

* Add new expenses
* View all expenses in table format
* Edit & delete expenses

📊 Dashboard

* Total expense calculation
* Clean UI for better experience
* Shows logged-in user's data

🗑️ Account Management

* Delete account feature
* Session handling for secure access

---

## 🛠️ Tech Stack

* 🐍 Python (Flask)
* 🗄️ MySQL
* 🎨 HTML + CSS
* ⚙️ Jinja2 Templates

---

## 📂 Project Structure

```
Expense_Tracker/
│
├── app.py
├── db.py
├── routes/
│   ├── auth_routes.py
│   └── expense_routes.py
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── index.html
│   └── edit.html
│
├── static/
│   └── style.css
│
└── .env (not included for security 🔒)
```

---

## ⚙️ Setup Instructions

1️⃣ Clone the repository

```
git clone https://github.com/Ashu-Backend/expense-tracker-flask.git
```

2️⃣ Install dependencies

```
pip install flask mysql-connector-python python-dotenv
```

3️⃣ Create `.env` file

```
SECRET_KEY=your_secret_key
DB_HOST=127.0.0.1
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=expense_db
```

4️⃣ Run the app

```
python app.py
```

---

## 🔐 Security Note

⚠️ Sensitive data like database credentials and secret keys are stored in `.env` file and not pushed to GitHub.

---

## 🚀 Future Improvements

* 📱 Responsive UI
* 📈 Charts & analytics
* 🔑 Password hashing
* 📧 Email verification system

---

## 🙌 Author

👤 Ashu  

💻 Passionate about coding & building real-world projects

---

⭐ If you like this project, don’t forget to star the repo!
