from . import db
from sqlalchemy.orm import backref

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

if __name__ == '__main__':
    app.run(debug=True)


class Estudante(db.Model):
    __tablename__ = 'Estudantes'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)

class Curso(db.Model):
    __tablename__ = 'Cursos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    duracao = db.Column(db.Integer, nullable=False)
    preco = db.Column(db.Float, nullable=False)

class Inscricao(db.Model):
    __tablename__ = 'Inscricoes'
    id = db.Column(db.Integer, primary_key=True)
    id_estudante = db.Column(db.Integer, db.ForeignKey('Estudantes.id'), nullable=False)
    id_curso = db.Column(db.Integer, db.ForeignKey('Cursos.id'), nullable=False)
    data_inscricao = db.Column(db.Date, nullable=False)

    estudante = db.relationship('Estudante', backref=db.backref('inscricoes', lazy=True))
    curso = db.relationship('Curso', backref=db.backref('inscricoes', lazy=True))





