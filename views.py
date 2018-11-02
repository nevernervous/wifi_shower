from app import app, db
from models import User


@app.route('/')
def index():
    return 'hello'
