import pytest
from src.db import get_db
from conftests import client, app


def test_index(client):
    response = client.get("/")
    assert b'Gerenciador de tarefas' in response.data


def test_create(client,  app):
    assert client.get("/create").status_code == 200
    
    response = client.post("/create", data={
        "title": "created", 
        "description": "whatever",
        "progress": "In Progress",
        "due_date": "01-01-2024"
    })
    with app.app_context():
        db = get_db()
        count = db.execute('SELECT COUNT(id) FROM tasks').fetchone()[0]
        assert count == 2


def test_update(client, app):
    assert client.get("/1/update").status_code == 200
    client.post("/1/update", data={
        "title": "updated", 
        "description": "",
        "progress": "",
        "due_date": ""
    })

    with app.app_context():
        db = get_db()
        task = db.execute('SELECT * FROM tasks WHERE id = 1').fetchone()
        print(80*'-')
        print(task["title"])
        assert task["title"] == "updated"


@pytest.mark.parametrize("path", (
    "/create",
    "/1/update",
))
def test_create_update_validate(client, path):
    response = client.post(path, data={
        "title": "", 
        "description": "",
        "progress": "",
        "due_date": ""
    })
    
    assert b"Obrigatorio ter titulo" in response.data

def test_delete(client, app):
    response = client.post("/1/delete")
    assert response.headers["Location"] == "/"

    with app.app_context():
        db = get_db()
        task = db.execute('SELECT * FROM tasks WHERE id = 1').fetchone()
        assert task is None