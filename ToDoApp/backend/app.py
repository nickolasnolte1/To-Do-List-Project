from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

# Route to fetch all tasks
@app.route('/api/todos', methods=['GET'])
def get_tasks():
    tasks = Todo.query.all()
    tasks_list = [{'id': task.id, 'title': task.title} for task in tasks]
    return jsonify(tasks_list)

# Route to add a task
@app.route('/api/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    if title:
        new_task = Todo(title=title)
        db.session.add(new_task)
        db.session.commit()
    return jsonify({"message": "Task added successfully"})

# Route to delete a task
@app.route('/api/delete/<int:id>', methods=['DELETE'])
def delete_task(id):
    task_to_delete = Todo.query.get_or_404(id)
    db.session.delete(task_to_delete)
    db.session.commit()
    return jsonify({"message": "Task deleted successfully"})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables if they don't exist
    app.run(host='0.0.0.0', port=5050)