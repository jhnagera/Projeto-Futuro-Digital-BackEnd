from flask import Flask
from conf.database import init_db

from control.funcionarios import funcionarios_bp
from control.login import login_bp


app = Flask(__name__)

#Conexao Geral do meu app
init_db(app)

#Registro de controladores 
app.register_blueprint(funcionarios_bp)
app.register_blueprint(login_bp)
app.register_blueprint(postos_bp)
#app.register_blueprint(pedidos_bp)


if __name__ == "__main__":
    app.run(debug=True)

