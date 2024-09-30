import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

database_url = os.getenv('DATABASE_URL')
if not database_url:
    raise RuntimeError("DATABASE_URL is not set. Flask cannot connect to a database!")

app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the Todo model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

# API route to fetch all tasks
@app.route('/api/todos', methods=['GET'])
def get_tasks():
    tasks = Todo.query.all()
    tasks_list = [{'id': task.id, 'title': task.title} for task in tasks]
    return jsonify(tasks_list)

# API route to add a new task
@app.route('/api/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    if title:
        new_task = Todo(title=title)
        db.session.add(new_task)
        db.session.commit()
    return jsonify({"message": "Task added successfully"})

# API route to delete a task
@app.route('/api/delete/<int:id>', methods=['DELETE'])
def delete_task(id):
    task_to_delete = Todo.query.get_or_404(id)
    db.session.delete(task_to_delete)
    db.session.commit()
    return jsonify({"message": "Task deleted successfully"})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables in PostgreSQL if they don't exist
    app.run(host='0.0.0.0', port=5050)