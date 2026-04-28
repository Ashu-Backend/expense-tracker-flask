from flask import render_template, request, redirect, url_for, Blueprint, session
from db import conn, cursor

expense_bp = Blueprint("expense", __name__)

@expense_bp.route("/home")
def home():
    print("Session User ID: ", session.get("user_id"))
    if "user_id" not in session:
        return redirect(url_for("auth.login"))
    else:
        cursor.execute(
            "SELECT * FROM expenses WHERE user_id = %s",
            (session["user_id"],)
            )
        data = cursor.fetchall()
        
        print("Data: ", data)
        cursor.execute("SELECT SUM(amount) FROM expenses WHERE user_id = %s", (session["user_id"],))
        total = cursor.fetchone()[0]
        total = total if total else 0
        return render_template("index.html", expenses = data, total=total)

@expense_bp.route("/add", methods=["GET", "POST"])
def add_expense():
    if request.method == "POST":
        title = request.form["title"]
        amount = float(request.form["amount"])

        if amount <= 0:
            return "Amount must be greater than 0"
        
        query = """
        INSERT INTO expenses (title, amount, date, user_id)
        VALUES (%s, %s, CURDATE(), %s)
        """

        cursor.execute(query, (title, amount, session["user_id"]))
        conn.commit()
        
        return redirect(url_for("expense.home"))
    
@expense_bp.route("/delete/<int:id>")
def delete_expense(id):
    query = "DELETE FROM expenses WHERE id = %s AND user_id = %s"
    cursor.execute(query, (id, session["user_id"]))
    conn.commit()
    
    return redirect(url_for("expense.home"))

@expense_bp.route("/edit/<int:id>")
def edit_expense(id):
    query = """SELECT * FROM expenses WHERE id = %s AND user_id = %s"""
    cursor.execute(query, (id, session["user_id"]))
    expense = cursor.fetchone()

    return render_template("edit.html", exp=expense)

@expense_bp.route("/update/<int:id>", methods=["POST"])
def update_expense(id):
    if request.method == "POST":
        title = request.form["title"]
        amount = float(request.form["amount"])
        
        if amount <= 0:
            return "Invalid amount"

        query = """UPDATE expenses 
        SET title = %s, amount = %s 
        WHERE id = %s AND user_id = %s"""
        
        cursor.execute(query, (title, amount, id, session["user_id"]))
        conn.commit()
        return redirect(url_for("expense.home"))