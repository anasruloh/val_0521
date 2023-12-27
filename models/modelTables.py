from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields, validate
 
db = SQLAlchemy()
 
class Task(db.Model):
 
    __tablename__ = 'tasks'
 
    task_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    done = db.Column(db.Boolean, default=False)
 
    def to_dict(self):
        return {
            'task_id': self.task_id,
            'title': self.title,
            'description': self.description,
            'done': self.done,
        }
    
 
class TaskSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Task
        load_instance = True
  
        
    title = fields.String(required = True, validate = validate.Length(min=1, error="Title cannot be empty"))
    description = fields.String(required = True, validate = validate.Length(min=1, error="desc cannot be empty"))
    done = fields.Boolean(required = True)