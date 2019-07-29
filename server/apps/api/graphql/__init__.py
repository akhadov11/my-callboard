from graphene import Schema, ObjectType

from .query import UserQuery

from .mutation import UserMutation


class Query(ObjectType, UserQuery):
    pass


class Mutation(ObjectType, UserMutation):
    pass


schema = Schema(query=Query, mutation=Mutation)


def get_snake_schema():
    return Schema(query=Query, mutation=Mutation, auto_camelcase=False)
