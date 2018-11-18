from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():

    return redirect(url_for("index"))    

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index")) 
