from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

receita_ingrediente = db.Table(
    'receita_ingrediente',
    db.Column('receita_id', db.Integer, db.ForeignKey('receita.id'), primary_key=True),
    db.Column('ingrediente_id', db.Integer, db.ForeignKey('ingrediente.id'), primary_key=True)
)

class Chef(db.Model):
    __tablename__ = 'chef'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)

    perfil = db.relationship('PerfilChef', back_populates='chef', uselist=False, cascade='all, delete-orphan')
    receitas = db.relationship('Receita', back_populates='chef', cascade='all, delete-orphan')

class PerfilChef(db.Model):
    __tablename__ = 'perfil_chef'
    id = db.Column(db.Integer, primary_key=True)
    especialidade = db.Column(db.String(120), nullable=False)
    anos_experiencia = db.Column(db.Integer, nullable=False)

    chef_id = db.Column(db.Integer, db.ForeignKey('chef.id'), unique=True, nullable=False)
    chef = db.relationship('Chef', back_populates='perfil')

class Receita(db.Model):
    __tablename__ = 'receita'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120), nullable=False)
    instrucoes = db.Column(db.Text, nullable=False)

    chef_id = db.Column(db.Integer, db.ForeignKey('chef.id'), nullable=False)
    chef = db.relationship('Chef', back_populates='receitas')

    ingredientes = db.relationship('Ingrediente', secondary=receita_ingrediente, back_populates='receitas')

class Ingrediente(db.Model):
    __tablename__ = 'ingrediente'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=True, nullable=False)

    receitas = db.relationship('Receita', secondary=receita_ingrediente, back_populates='ingredientes')