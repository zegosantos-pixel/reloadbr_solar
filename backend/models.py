from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
db = SQLAlchemy()

class Provider(db.Model):
    __tablename__ = 'providers'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    estado = db.Column(db.String(4), nullable=False)
    preco_kwh = db.Column(db.Float, nullable=True)
    beneficios = db.Column(db.Text, nullable=True)
    site = db.Column(db.String(512), nullable=True)
    relevancia = db.Column(db.Integer, default=0)
    updated_at = db.Column(db.DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'estado': self.estado,
            'preco_kwh': self.preco_kwh,
            'beneficios': self.beneficios,
            'site': self.site,
            'relevancia': self.relevancia
        }

    @classmethod
    def from_dict(cls, d):
        return cls(
            nome=d.get('nome'),
            estado=d.get('estado'),
            preco_kwh=d.get('preco_kwh'),
            beneficios=d.get('beneficios'),
            site=d.get('site'),
            relevancia=d.get('relevancia', 0)
        )
