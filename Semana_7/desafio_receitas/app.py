import os
from flask import Flask, request, redirect, url_for, render_template, flash
from models import db, Chef, PerfilChef, Receita, Ingrediente

app = Flask(__name__)
app.config['SECRET_KEY'] = 'uma-chave-secreta-bem-segura'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    receitas = Receita.query.all()
    return render_template('index.html', receitas=receitas)

@app.route('/receita/nova', methods=['GET', 'POST'])
def criar_receita():
    chefs = Chef.query.all()
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        instrucoes = request.form.get('instrucoes')
        chef_id = request.form.get('chef_id')
        ingredientes_texto = request.form.get('ingredientes')

        if titulo and instrucoes and chef_id:
            nova_receita = Receita(titulo=titulo, instrucoes=instrucoes, chef_id=chef_id)

            if ingredientes_texto:
                nomes = [n.strip() for n in ingredientes_texto.split(',') if n.strip()]
                for nome in nomes:
                    ingr = Ingrediente.query.filter_by(nome=nome).first()
                    if not ingr:
                        ingr = Ingrediente(nome=nome)
                        db.session.add(ingr)
                    nova_receita.ingredientes.append(ingr)

            db.session.add(nova_receita)
            db.session.commit()
            flash("Receita criada com sucesso!", "success")
            return redirect(url_for('index'))

    return render_template('criar_receita.html', chefs=chefs)

@app.route('/chef/novo', methods=['GET', 'POST'])
def criar_chef():
    if request.method == 'POST':
        nome = request.form.get('nome')
        especialidade = request.form.get('especialidade')
        anos_experiencia = request.form.get('anos_experiencia')

        if nome and especialidade and anos_experiencia:
            novo_chef = Chef(nome=nome)
            perfil = PerfilChef(
                especialidade=especialidade,
                anos_experiencia=int(anos_experiencia),
                chef=novo_chef
            )
            db.session.add(novo_chef)
            db.session.add(perfil)
            db.session.commit()
            flash("Chef cadastrado com sucesso!", "success")
            return redirect(url_for('index'))

    return render_template('criar_chef.html')

@app.route('/chef/<int:chef_id>')
def detalhes_chef(chef_id):
    chef = Chef.query.get_or_404(chef_id)
    return render_template('detalhes_chef.html', chef=chef)

@app.route('/receita/<int:receita_id>')
def detalhes_receita(receita_id):
    receita = Receita.query.get_or_404(receita_id)
    return render_template('detalhes_receita.html', receita=receita)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5002)