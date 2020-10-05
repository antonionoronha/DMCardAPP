from DMCard.restplus import api
from flask_restplus import Resource
from DMCard.serializers.solicitation import solicitation_serializer
from DMCard.business.solicitation import SolicitationBus
from flask_cors import CORS, cross_origin

ns_solicitation = api.namespace('solicitations',
                            description='Operations related to solicitations')

@ns_solicitation.route('/')
class SolicitationCollection(Resource):

    def __init__(self, api=None, *args, **kwargs):
        super(SolicitationCollection, self).__init__(api, args, kwargs)
        self.bus = SolicitationBus()

    @api.marshal_list_with(solicitation_serializer)
    def get(self):
        return self.bus.get_all()

    @api.expect(solicitation_serializer)
    @api.marshal_with(solicitation_serializer, code=201)
    def post(self):
        return self.bus.add(api.payload['client'],api.payload['address'],api.payload['income'])

@ns_solicitation.route('/<int:id>')
@api.response(404, 'Solicitation not found.')
class SolicitationItem(Resource):

    def __init__(self, api=None, *args, **kwargs):
        super(SolicitationItem, self).__init__(api, args, kwargs)
        self.bus = SolicitationBus()

    @api.marshal_with(solicitation_serializer)
    def get(self, id):
        return self.bus.get_by_id(id)

    @api.marshal_with(solicitation_serializer)
    def delete(self, id):
        return self.bus.delete_by_id(id)