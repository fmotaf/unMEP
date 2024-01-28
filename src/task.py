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
        ' ORDER BY created_at DESC'
    ).fetchall()
    return render_template("task/index.html", tasks=tasks)


@bp.route("/create", methods=("GET","POST"))
def create():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        progress = request.form["progress"]
        due_date = request.form["due_date"]
        error = None
        
        if not title:
            error = "Obrigatorio ter titulo"
            print(error)

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
            return redirect(url_for("task.index"))

    return render_template("task/create.html")


def get_task(id, check_author=True):
    task = get_db().execute(
        'SELECT t.id, title, description_, progress, due_date'
        ' FROM tasks t WHERE t.id = ?',
        (id,)
    ).fetchone()

    if task is None:
        abort(404, f"Task de id {id} não existe.")

    return task


@bp.route("/<int:id>/update", methods = ("POST", "GET"))
def update(id):
    task = get_task(id)

    if request.method == "POST":
        title       = request.form["title"]
        description = request.form["description"]
        progress    = request.form["progress"]
        due_date    = request.form["due_date"]
        error       = None

        if not title:
            error = "Obrigatorio ter titulo"
        
        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE tasks SET title = ?, description_ = ?, progress = ?, due_date = ?, updated_at = CURRENT_TIMESTAMP'
                ' WHERE id = ?',
                (title, description, progress, due_date, id)
            )
            db.commit()
            return redirect(url_for("task.index"))
    
    return render_template("task/update.html", task=task)

@bp.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    get_task(id)
    db = get_db()
    db.execute('DELETE FROM tasks WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('task.index'))