import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


load_dotenv()

app = Flask(__name__)
app.config.from_object(os.getenv('APP_SETTINGS', 'config.ProductionConfig'))


db = SQLAlchemy(app)
migrate = Migrate(app, db)


import models, views


if __name__ == '__main__':
    app.run()
