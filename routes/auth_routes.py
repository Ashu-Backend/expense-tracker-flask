from flask import Blueprint, render_template, request, redirect, url_for, session
from db import conn, cursor

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        query = """SELECT * FROM users WHERE username = %s AND password = %s"""
        cursor.execute(query, (username, password))
        user = cursor.fetchone()
        if user:
            session["user"] = username
            session["user_id"] = user[0]
            return redirect(url_for("expense.home"))
        else:
            return "Invalid Credentials"
            
    return render_template("login.html")

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        existing_user = cursor.fetchone()
        
        if existing_user:
            return render_template("register.html", error="User already exists")

        query = """INSERT INTO users (username, password) VALUES (%s, %s)"""
        cursor.execute(query, (username, password))
        conn.commit()
        
        return redirect(url_for("auth.login"))
        
    return render_template("register.html")

@auth_bp.route("/logout", methods=["GET", "POST"])
def logout():
    session.clear()
    session.pop("user", None)
    return redirect(url_for("auth.login"))
        
        
@auth_bp.route("/delete-account", methods=["POST"])
def delete_account():
    user_id = session.get("user_id")

    if user_id:
        cursor.execute(
            "DELETE FROM users WHERE id = %s",
            (user_id,)
        )
        conn.commit()
        
        session.clear()
        return redirect(url_for("auth.login"))
    return "User not found"