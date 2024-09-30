from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Crear la app Flask
app = Flask(__name__)

# Configurar la base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la base de datos
db = SQLAlchemy(app)

# Modelo de la base de datos
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Todo {self.id}>'

# Ruta para la página principal
@app.route('/')
def index():
    # Obtener todas las tareas de la base de datos
    tasks = Todo.query.all()
    return render_template('index.html', tasks=tasks)

# Ruta para añadir nuevas tareas
@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    new_task = Todo(title=title)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('index'))

# Ruta para borrar tareas
@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crear las tablas si no existen
    app.run(debug=True)