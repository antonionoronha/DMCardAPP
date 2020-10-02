from DMCard.restplus import api
from flask_restplus import fields

solicitation_serializer = api.model('Solicitation', {
    'id': fields.Integer(readonly=True),
    'client': fields.String(required=True, description='Nome do cliente'),
    'address': fields.String(required=True, description='Endereço do cliente'),
    'income': fields.Float(required=True, description='Renda do cliente'),
    'status': fields.String(readonly=True, description="Status da solicitação"),
    'credit': fields.Float(readonly=True, description="Crédito do cliente"),
    'score': fields.Integer(readonly=True, description="Score do cliente")
})
