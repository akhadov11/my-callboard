from django.contrib.auth import get_user_model

from graphene import Field, Int

from apps.api.graphql.types import nodes
from apps.api.graphql.utils.decorators import is_authenticated, is_staff

User = get_user_model()


class UserQuery(object):
    current_user = Field(lambda: nodes.UserNode)
    user = Field(lambda: nodes.UserNode, user_id=Int(required=True))

    @is_staff(raise_exception=True)
    def resolve_user(self, _, user_id):
        return User.objects.get(id=user_id)

    @is_authenticated(raise_exception=True)
    def resolve_current_user(self, info):
        return info.context.user
