from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class ReceitaForm(FlaskForm):
    nome_receita = StringField('Nome da Receita', validators=[DataRequired(message='Por favor, insira o nome da receita.')])
    ingredientes = TextAreaField('Ingredientes', validators=[DataRequired(message='Por favor, insira os ingredientes.')])
    modo_preparo = TextAreaField('Modo de Preparo', validators=[DataRequired(message='Por favor, insira o modo de preparo.')])
    submit = SubmitField('Enviar')