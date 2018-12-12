from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.projects.models import Project
from application.projects.forms import ProjectForm


@app.route("/projects/", methods=["GET"])
@login_required
def projects_index():
    return render_template("projects/list.html", projects = Project.query.all())

@app.route("/projects/<project_id>/", methods=["GET"])
@login_required
def projects_show(project_id):
    return render_template("projects/edit.html", form = ProjectForm(), project = Project.query.get(project_id))

@app.route("/projects/new/")
@login_required
def projects_form():
    return render_template("projects/new.html", form = ProjectForm())

@app.route("/projects/togglecomplete/<project_id>", methods=["GET"])
@login_required
def projects_set_done(project_id):

    t = Project.query.get(project_id)
    if(t.done):
        t.done = False
    else:
        t.done = True 
   
    db.session().commit()
  
    return redirect(url_for('projects_show', project_id=project_id))

@app.route("/projects/morehours/<project_id>", methods=["GET"])
@login_required
def projects_set_more_hours(project_id):

    t = Project.query.get(project_id)
    t.time = t.time + 1
    db.session().commit()
  
    return redirect(url_for('projects_show', project_id=project_id))

@app.route("/projects/lesshours/<project_id>", methods=["GET"])
@login_required
def projects_set_less_hours(project_id):

    t = Project.query.get(project_id)
    if(t.time > 0):
        t.time = t.time - 1
        
    db.session().commit()
  
    return redirect(url_for('projects_show', project_id=project_id))


@app.route("/projects/delete/<project_id>/", methods=["GET"])
@login_required
def projects_set_delete(project_id):

    t = Project.query.get(project_id)
   
    db.session.delete(t)
    db.session().commit()
  
    return redirect(url_for("projects_index"))
  
@app.route("/projects", methods=["POST"])
@login_required
def projects_create():
    form = ProjectForm(request.form)

    if not form.validate():
        return render_template("projects/new.html", form = form)
  
    t = Project(form.name.data)
    t.done = form.done.data
    t.time = form.time.data
    t.name = form.name.data
    t.account_id = current_user.id
    
    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("projects_index"))

@app.route("/projects/edit/<project_id>/", methods=["POST"])
@login_required
def projects_edit_name():
    form = ProjectForm(request.form)

    if not form.validate():
        return render_template("projects/new.html", form = form)
  
    t = Project(form.name.data)
    t.done = form.done.data
    t.time = form.time.data
    t.name = form.name.data    
    db.session().commit()
  
    return redirect(url_for("projects_index"))
