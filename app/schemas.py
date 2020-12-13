from app import ma
from app.models import Sistema, PmlMdaSin

class SistemaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Sistema
    id = ma.auto_field()
    short_name = ma.auto_field()
    nombre = ma.auto_field()

class PmlMdaSinSchema(ma.SQLAlchemySchema):
    class Meta:
        model = PmlMdaSin
    fecha = ma.auto_field()
    pml = ma.auto_field()
    # id_sistema = ma.auto_field()
    # sistema = ma.Nested(SistemaSchema(only=['nombre']))
    sistema = ma.Pluck(SistemaSchema, 'nombre')