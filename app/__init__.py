# __init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api

db = SQLAlchemy()

# Initialize the API here
api = Api(
    title='Inventory Management API',
    version='1.0',
    description='A simple Inventory Management API for CPSC 449 Assignment 1.'
)

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    db.init_app(app)

    # Now you can import the namespaces
    from .routes import ns as inventory_ns
    api.add_namespace(inventory_ns)

    # Attach the API to the app
    api.init_app(app)

    return app
