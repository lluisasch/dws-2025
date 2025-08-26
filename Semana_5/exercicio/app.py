import os
from flask import Flask, render_template, request, redirect, url_for, flash

from forms import ReceitaForm

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24);

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/receita', methods=['POST', 'GET'])
def receita():
    form = ReceitaForm()
    if form.validate_on_submit():
        nome_receita = form.nome_receita.data
        ingredientes = form.ingredientes.data
        modo_preparo = form.modo_preparo.data
        
        print(f'Receita: {nome_receita}')
        print(f'Ingredientes: {ingredientes}')
        print(f'Modo de Preparo: {modo_preparo}')
        
        flash('Receita cadastrada com sucesso!', 'success')
        return redirect(url_for('receita_criada', nome_receita=nome_receita, ingredientes=ingredientes, modo_preparo=modo_preparo))
    
    return render_template('receita.html', form=form)

@app.route('/receita_criada')
def receita_criada():
    nome_receita = request.args.get('nome_receita', '')
    ingredientes = request.args.get('ingredientes', '')
    modo_preparo = request.args.get('modo_preparo', '')
    return render_template('receita_criada.html', nome_receita=nome_receita, ingredientes=ingredientes, modo_preparo=modo_preparo)   

if __name__ == '__main__':
    app.run(debug=True)