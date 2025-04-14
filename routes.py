from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Task

routes = Blueprint("routes", __name__)

@routes.route('/')
def home():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@routes.route('/add', methods=['POST'])
def add_task():
    title = request.form['title']
    description = request.form.get('description', "")
    new_task = Task(title=title, description=description)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('routes.home'))

@routes.route('/complete/<int:task_id>')
def complete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        task.completed = True
        db.session.commit()
    return redirect(url_for('routes.home'))

@routes.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('routes.home'))