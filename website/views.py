from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Project, ToDo
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        project = request.form.get('project')

        if len(project) < 1:
            flash('Project title is too short.', category='error')
        else:
            new_project = Project(title=project, user_id=current_user.id)
            db.session.add(new_project)
            db.session.commit()
            flash('Project added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/delete-project', methods=['POST'])
def delete_project():
    project = json.loads(request.data)
    projectId = project['projectId']
    project = Project.query.get(projectId)
    if project:
        if project.user_id == current_user.id:
            db.session.delete(project)
            db.session.commit()
            
    return jsonify({})

@views.route('/<project_title>', methods=['GET', 'POST'])
def project_page(project_title):
    project = Project.query.filter_by(title=project_title).first()
    if project:
        if request.method == 'POST':
            todo = request.form.get('todo')

            if len(todo) < 1:
                flash('note is too short.', category='error')
            else:
                new_todo = ToDo(data=todo, project_id=project.id)
                db.session.add(new_todo)
                db.session.commit()
                flash('Note added!', category='success')
        return render_template("project.html", user=current_user, project=project)

@views.route('/delete-todo', methods=['POST'])
def delete_todo():
    todo = json.loads(request.data)
    print(todo)
    todoId = todo['todoId']
    print(todoId)
    todo = ToDo.query.get(todoId)
    if todo:
        db.session.delete(todo)
        db.session.commit()
            
    return jsonify({})