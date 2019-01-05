import datetime as dt

from flasgger import swag_from
from flask_restful import Resource
from webargs import fields, ValidationError
from webargs.flaskparser import use_kwargs

from common.config import default_encoding
from common.utils import parse


def validate_date(date):
    try:
        return dt.datetime.strptime(date, '%d.%m.%Y')
    except ValueError:
        raise ValidationError('Invalid date format.')


class Group(Resource):
    args = {
        'group': fields.Str(required=True),
        'from_date': fields.Str(required=True, validate=validate_date),
        'to_date': fields.Str(required=True, validate=validate_date)
    }

    @staticmethod
    @use_kwargs(args)
    @swag_from('../docs/group.yaml')
    def get(group, from_date, to_date):
        result = parse({'group': group.encode(default_encoding)}, from_date, to_date)
        if result:
            return result, 200
        return {'error': 'Schedule not found'}, 404


class Teacher(Resource):
    args = {
        'teacher': fields.Str(required=True),
        'from_date': fields.Str(required=True, validate=validate_date),
        'to_date': fields.Str(required=True, validate=validate_date)
    }

    @staticmethod
    @use_kwargs(args)
    @swag_from('../docs/teacher.yaml')
    def get(teacher, from_date, to_date):
        result = parse({'teacher': teacher.encode(default_encoding)}, from_date, to_date)
        if result:
            return result, 200
        return {'error': 'Schedule not found'}, 404
