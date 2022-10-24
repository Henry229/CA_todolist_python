from datetime import datetime
from flask import Blueprint, request, render_template, flash, session, redirect, url_for
from db import db, ma 
from models.todo import Todo, TodoSchema

todo_bp = Blueprint('todos', __name__)

@todo_bp.route('/')
def home():
    if session.get('registered'):
        return render_template('home.html')
    else:
        return render_template('home.html')
      
    # stmt = db.select(Todo).order_by(Todo.id)
    # todos = db.session.scalars(stmt)
    # return TodoSchema(many=True).dump(todos)
  
@todo_bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        job = request.form.get('job')
        date = datetime.today()
        new_job = Todo(job=job, date=date)
        db.session.add(new_job)
        db.session.commit()
        # session['registered'] = True
        flash('New job created successfully')
        return redirect(url_for('todos.home'))
    else:
        return render_template('add.html')  
  