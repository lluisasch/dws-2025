from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo

#Criando/instanciando a aplicação Flask
app = Flask(__name__)

app.config['SECRET_KEY'] = 'uma_chave_de_segurança_muito_dificil'

class MeuFormulario(FlaskForm):
    nome = StringField('Nome completo', validators=[
        DataRequired(message='Campo obrigatório')
    ])
    email = StringField('E-mail', validators=[
        DataRequired(message='Campo obrigatório'),
        Email(message='Por favor, insira um email válido.')
    ])
    submit = SubmitField("Enviar")

class FormularioRegistro(FlaskForm):
    nome = StringField('Nome completo', validators=[
        DataRequired(message='Campo obrigatório')
    ])
    email = StringField('E-mail', validators=[
        DataRequired(message='Campo obrigatório'),
        Email(message='Por favor, insira um email válido.')
    ])
    senha = PasswordField('Senha', validators=[
        DataRequired(message="Campo obrigatório"),
        Length(min=8, message="A senha deve ter pelo menos 8 caracteres")
    ])
    confirmar_senha = PasswordField('Confirmar Senha', validators=[
        DataRequired(message="Campo obrigatório"),
        EqualTo('senha', message="As senhas devem ser iguais")
    ])
    biografia = TextAreaField('Biografia (opcional)')
    aceitar_termos = BooleanField('Aceito os Termos de Serviço', validators=[
        DataRequired(message="Você deve aceitar os termos para continuar")
    ])
    submit = SubmitField("Registrar")
    
# Definindo as rotas
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    form = MeuFormulario()
    
    if form.validate_on_submit():
        nome_usuario = form.nome.data
        email_usuario = form.email.data
        flash(f'Cadastro recebido para {nome_usuario} e {email_usuario}')
        return redirect(url_for('formulario'))
    
    return render_template('formulario.html', form=form)

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    form = FormularioRegistro()
    if form.validate_on_submit():
        nome_usuario = form.nome.data
        bio = form.biografia.data.strip() if form.biografia.data else None

        if bio:
            flash(f"Bem-vindo(a), {nome_usuario}! Obrigado por se registrar. Sua biografia: {bio[:60]}...")
        else:
            flash(f"Bem-vindo(a), {nome_usuario}! Obrigado por se registrar.")
        return redirect(url_for('registro'))
    
    return render_template('registro.html', form=form)


# Definindo a execução app flask
if __name__ == '__main__':
    app.run(debug=True)