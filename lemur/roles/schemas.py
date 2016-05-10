"""
.. module: lemur.roles.schemas
    :platform: unix
    :copyright: (c) 2015 by Netflix Inc., see AUTHORS for more
    :license: Apache, see LICENSE for more details.
.. moduleauthor:: Kevin Glisson <kglisson@netflix.com>
"""
from marshmallow import fields
from lemur.common.schema import LemurInputSchema, LemurOutputSchema
from lemur.schemas import AssociatedUserSchema, AssociatedAuthoritySchema


class RoleInputSchema(LemurInputSchema):
    name = fields.String(required=True)
    username = fields.String()
    password = fields.String()
    description = fields.String()
    authorities = fields.Nested(AssociatedAuthoritySchema, many=True)
    users = fields.Nested(AssociatedUserSchema, many=True)


class RoleOutputSchema(LemurOutputSchema):
    name = fields.String()
    username = fields.String()
    password = fields.String()
    description = fields.String()
    authorities = fields.Nested(AssociatedAuthoritySchema, many=True)
    users = fields.Nested(AssociatedUserSchema, many=True)
    users = fields.Nested(AssociatedUserSchema, many=True)


role_input_schema = RoleInputSchema()
role_output_schema = RoleOutputSchema()
roles_output_schema = RoleOutputSchema(many=True)