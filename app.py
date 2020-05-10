from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://apple@localhost:5432/todoapp'
db = SQLAlchemy(app)


class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)

    # Dander-repr method
    def __repr__(self):
        return f'<Todo {self.id} {self.description}>'


# Create table
db.create_all()

# Route for /todos/create
@app.route('/todos/create', methods=['POST'])
# Route for index
@app.route('/')
def index():
    return render_template('index.html', data=Todo.query.all())
