from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:123@localhost/projeto_escala'

    db.init_app(app)