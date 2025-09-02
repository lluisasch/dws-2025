# -*- coding: utf-8 -*-

# Passo 1: Importações e Configuração
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
# Inicializa a aplicação Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Sua-Segurança-Mora-Aqui'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meuapp.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    def __repr__(self):
        return f'<Usuario {self.nome}>'
    
class Postagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120), nullable=False)
    conteudo = db.Column(db.Text, nullable=False)
    data_publicacao = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Postagem {self.titulo}>'
    
    def __repr__(self):
        return f'<Postagem {self.conteudo}>'
# --- Rotas da Aplicação ---

# Rota principal que exibe o formulário e a lista de usuários
@app.route('/')
def index():
    usuarios = Usuario.query.all()
    return render_template('index.html', usuarios=usuarios)

# Rota para adicionar um novo usuário
@app.route('/adicionar', methods=['POST'])
def adicionar_usuario():
    nome = request.form['nome']
    email = request.form['email']
    novo_usuario = Usuario(nome=nome, email=email)
    db.session.add(novo_usuario)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/postagem', methods=['GET'])
def postagem():
    postagens = Postagem.query.all()
    return render_template('postagem.html', postagens=postagens)
# Rota para adicionar uma nova postagem
@app.route('/postagem', methods=['POST'])
def adicionar_postagem():
    titulo = request.form['titulo']
    conteudo = request.form['conteudo']
    data_publicacao = datetime.utcnow()
    nova_postagem = Postagem(titulo=titulo, conteudo=conteudo, data_publicacao=data_publicacao)
    db.session.add(nova_postagem)
    db.session.commit()
    return redirect(url_for('postagem'))
 
# Passo 3: Criando o Banco de Dados Físico
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    
    # Inicia o servidor de desenvolvimento do Flask
    app.run(host='0.0.0.0', port=5000, debug=True)
