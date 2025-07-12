from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import datetime

# Inicializa a app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'segredo_seguro'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rh_core.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Base de dados
db = SQLAlchemy(app)

# Definir modelo
class RecursoHumano(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.String(100))
    n_mec = db.Column(db.String(50))
    nome = db.Column(db.String(200))
    funcao = db.Column(db.String(100))
    edei_utilizador = db.Column(db.String(100))
    observacoes = db.Column(db.Text)
    situacao_atual = db.Column(db.String(100))
    horas_semana = db.Column(db.Float)
    outros_dados = db.Column(db.Text)
    data_nascimento = db.Column(db.Date)
    idade = db.Column(db.Integer)
    inicio_atividade_jcs = db.Column(db.Date)
    anos_atividade = db.Column(db.Integer)
    inicio_atividade_core = db.Column(db.Date)
    fim_atividade_core = db.Column(db.Date)
    email_pessoal = db.Column(db.String(200))
    email_jcs = db.Column(db.String(200))
    telemovel = db.Column(db.String(20))

# Interface administrativa
admin = Admin(app, name='RH CORE', template_mode='bootstrap4')
admin.add_view(ModelView(RecursoHumano, db.session))

# Executar app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

