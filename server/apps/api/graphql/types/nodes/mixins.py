from graphene import Int


class IdMixin(object):
    id = Int(required=True)
