from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from src.db import get_db

bp = Blueprint("task", __name__)

@bp.route("/")
def index():
    db = get_db()
    tasks = db.execute(
        'SELECT t.id, title, description_, progress, due_date'
        ' FROM tasks t '
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template("task_form.html", tasks=tasks)

@bp.route("/create", methods=("GET","POST"))
def create():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        progress = request.form["progress"]
        due_date = request.form["description"]
        error = None

        if not title:
            error = "Title is required"
        
        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO tasks (title, description_, progress, due_date)'
                ' VALUES (?, ?, ?, ?)',
                (title, description, progress, due_date)
            )
            db.commit()
            return redirect(url_for("task.create"))
    
    db = get_db()
    tasks = db.execute(
        'SELECT t.id, title, description_, progress, due_date'
        ' FROM tasks t '
        ' ORDER BY created DESC'
    ).fetchall()

    return render_template("task_form.html", tasks=tasks)