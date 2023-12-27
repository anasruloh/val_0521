from flask import Blueprint
from controllers.TasksController import index, store, show, update, delete

task_bp = Blueprint('task_bp', __name__)

task_bp.route('/', methods=['GET'])(index)
task_bp.route('/', methods=['POST'])(store)
task_bp.route('/<int:task_id>', methods=['GET'])(show)
task_bp.route('/<int:task_id>', methods=['PUT'])(update)
task_bp.route('/<int:task_id>', methods=['DELETE'])(delete)
