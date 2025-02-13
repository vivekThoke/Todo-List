from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

db_path = os.path.join('/tmp', 'tasks.db')
app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{db_path}'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def home():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        task_description = request.form.get('task')
        if task_description:
            new_task = Task(description=task_description)
            db.session.add(new_task)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_task.html')

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = Task.query.get(task_id)
    if request.method == 'POST':
        task_description = request.form.get('task')
        if task_description:
            task.description = task_description
            db.session.commit()
            return redirect(url_for('home'))
    return render_template('edit_task.html', task=task)

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)