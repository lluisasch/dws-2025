import os
from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, DateField, SelectField, ValidationError
from wtforms.validators import DataRequired, Email
from datetime import datetime

# --- Configuração da Aplicação Flask ---
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

def validate_data_evento(form, field):
    data_evento = field.data
    if data_evento < datetime.today().date():
        raise ValidationError('A data do evento não pode ser no passado.')
    
def validate_descricao(form, field):
    if form.tipo_evento.data == 'Outro' and not field.data:
        raise ValidationError('A descrição é obrigatória para o tipo de evento "Outro".')
    
class EventoForm(FlaskForm):
    nome_evento = StringField('Nome do Evento', validators=[DataRequired(message="O campo nome do evento é obrigatório.")])
    data_evento = DateField('Data do Evento', validators=[DataRequired(message="O campo data do evento é obrigatório."), validate_data_evento])
    organizador = StringField('Organizador', validators=[DataRequired(message="O campo organizador é obrigatório.")])
    tipo_evento = SelectField('Tipo de Evento', choices=['Palestra', 'Reunião', 'Outro'])
    mensagem = TextAreaField('Mensagem')
    enviar = SubmitField('Enviar')
    descricao = TextAreaField('Descrição', validators=[validate_descricao])
    
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
    
    form = EventoForm()
    if form.validate_on_submit():
        nome_evento = form.nome_evento.data
        return render_template('sucesso.html', nome_evento=nome_evento)
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