from flask import Flask
from flask_migrate import Migrate
from models.modelTables import db
from routes.task_bp import task_bp

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(task_bp, url_prefix='/tasks')

if __name__ == '__main__':
	app.run(port=4000, debug=True)