from flask_sqlalchemy import SQLAlchemy
from flask import jsonify, request
from models.modelTables import Task, db

db = SQLAlchemy()

def index():
    tasks = Task.query.all()
    response = [task.to_dict() for task in tasks]
    return jsonify(response)

def store():
    request_json = request.get_json()
    new_task = Task(
        title=request_json['title'],
        description=request_json['description'],
        done=bool(request_json['done'])
    )
    db.session.add(new_task)
    db.session.commit()
    response = new_task.to_dict()
    return jsonify(response)

def show(task_id):
    task = Task.query.get(task_id)
    if task:
        response = task.to_dict()
        return jsonify(response)
    else:
        return jsonify({"error": "Data Not Found"}), 404

def update(task_id):
    task = Task.query.get(task_id)
    if task:
        request_json = request.get_json()
        task.title = request_json.get('title', task.title)
        task.description = request_json.get('description', task.description)
        task.done = request_json.get('done', task.done)
        db.session.commit()
        response = task.to_dict()
        return jsonify(response)
    else:
        return jsonify({"error": "Data Not Found"}), 404

def delete(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
        return jsonify({"message": f"Task dengan id {task_id} berhasil dihapus"})
    else:
        return jsonify({"error": "Data Not Found"}), 404
