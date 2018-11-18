from flask import render_template, request, redirect, url_for

from application import app, db
from application.tasks.models import Task
from application.tasks.forms import TaskForm

@app.route("/tasks/new/")
def tasks_form():
    return render_template("tasks/new.html", form = TaskForm())

@app.route("/")
def index():
    return render_template("index.html")
