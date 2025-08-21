import os
from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

# --- Configuração da Aplicação Flask ---
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
# --- Definição do Formulário com WTForms ---
class ContatoForm(FlaskForm):
    nome = StringField('Nome',
    validators=[DataRequired(message="O campo nome é obrigatório.")]
)
    email = StringField('E-mail',
    validators=[
    DataRequired(message="O campo e-mail é obrigatório."),
    Email(message="Por favor, insira um e-mail válido.")]
)
    mensagem = TextAreaField('Mensagem')
    enviar = SubmitField('Enviar')
    
# --- Definição de um Objeto para Simulação ---
class Usuario:
    def __init__(self, nome, email, mensagem=""):
        self.nome = nome
        self.email = email
        self.mensagem = mensagem
# --- Rotas da Aplicação ---
@app.route("/")
def index():
    return render_template('index.html')
@app.route("/vazio", methods=['GET', 'POST'])
def formulario_vazio():
    
    form = ContatoForm()
    if form.validate_on_submit():
        nome_usuario = form.nome.data
        return render_template('sucesso.html', nome_usuario=nome_usuario)
    return render_template('formulario.html', form=form, title="1. Formulário Vazio")

@app.route("/via-argumentos", methods=['GET', 'POST'])
def formulario_via_argumentos():

    form = ContatoForm() 
    if form.validate_on_submit():
        nome_usuario = form.nome.data
        return render_template('sucesso.html', nome_usuario=nome_usuario)

    elif not form.is_submitted():
        dados_iniciais = {
        'nome': 'João da Silva',
        'email': 'joao.silva@email.com',
        'mensagem': 'Esta é uma mensagem preenchida por argumentos.'}
        
    form = ContatoForm(**dados_iniciais)
    return render_template('formulario.html', form=form, title="2. Formulário Preenchido via Argumentos")
@app.route("/via-objeto", methods=['GET', 'POST'])
def formulario_via_objeto():
    form = ContatoForm()
    if form.validate_on_submit():
        nome_usuario = form.nome.data
        return render_template('sucesso.html', nome_usuario=nome_usuario)
    elif not form.is_submitted():
        usuario_mock = Usuario(
        nome="Maria Oliveira",
        email="maria.o@email.net",
        mensagem="Mensagem vinda de um objeto.")
        
    form = ContatoForm(obj=usuario_mock)
    return render_template('formulario.html', form=form, title="3. Formulário Preenchido via Objeto")

if __name__ == '__main__':
    app.run(debug=True)