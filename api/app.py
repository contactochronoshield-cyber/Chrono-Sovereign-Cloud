from flask import Flask, render_template, request, redirect, session
import sqlite3
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.secret_key = "ChronoShieldSecret2026"

DB = "database/chrono.db"

@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect(DB)
        cur = conn.cursor()

        cur.execute(
            "SELECT password FROM users WHERE username=?",
            (username,)
        )

        user = cur.fetchone()

        conn.close()

        if user and check_password_hash(user[0], password):

            session["user"] = username

            return redirect("/dashboard")

        return render_template(
            "login.html",
            error="Credenciales incorrectas"
        )

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect("/")

    return render_template(
        "dashboard.html",
        user=session["user"]
    )

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")

@app.route("/health")
def health():

    return {
        "status":"online",
        "platform":"Chrono Sovereign Cloud"
    }

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
