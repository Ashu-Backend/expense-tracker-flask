from flask import Flask
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

app.config['SECRET_KEY'] = os.getenv("secret_key")

from routes.auth_routes import auth_bp
app.register_blueprint(auth_bp)

from routes.expense_routes import expense_bp
app.register_blueprint(expense_bp)

if __name__=="__main__":
    app.run(debug=True)