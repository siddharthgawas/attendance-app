from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config.from_object('attendance_app.config')
db = SQLAlchemy(app)
db.Model.metadata.reflect(db.engine)
import attendance_app.models
import attendance_app.views
