from flask_restx import Namespace, fields
from flask_restx.inputs import boolean

__all__ = [
    'users_ns',
    'user_model',
    'users_list_response',
]

users_ns = Namespace('users', description='API endpoints to handle users')

geo_model = users_ns.model('Geo', {
    'lat': fields.Float,
    'lng': fields.Float,
})

address_model = users_ns.model('Address', {
    'street': fields.String,
    'suite': fields.String,
    'city': fields.String,
    'zipcode': fields.String,
    'geo': fields.Nested(geo_model),
})

company_model = users_ns.model('Company', {
    'name': fields.String,
    'catchPhrase': fields.String,
    'bs': fields.String,
})

user_model = users_ns.model('User', {
    'id': fields.Integer(min=0),
    'name': fields.String,
    'username': fields.String,
    'email': fields.String,
    'address': fields.Nested(address_model),
    'phone': fields.String,
    'website': fields.String,
    'company': fields.Nested(company_model),
})

users_list_response = users_ns.model(
    'User List Response', {
        'total_items': fields.Integer,
        'data:': fields.List(
            fields.Raw(),
            description='List of users'
        )
    }
)
