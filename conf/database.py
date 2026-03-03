from flask_sqlalchemy import SQLAlchemy

load_dotenv()

db = SQLAlchemy()

def init_db(app):
    database_url = os.getenv('DATABASE_URL')


    if not database_url:
        raise ValueError("DATABASE_URL não encontrado no arquivo .env")
    
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url

    db.init_app(app)