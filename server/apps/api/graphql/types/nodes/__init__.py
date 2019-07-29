from django.contrib.auth import get_user_model

from graphene import String

from graphene_django.types import DjangoObjectType

from apps.api.graphql.types.nodes.mixins import IdMixin

User = get_user_model()


class UserNode(IdMixin, DjangoObjectType):
    class Meta:
        model = User
        exclude_fields = ("password", "is_staff", "is_superuser")

    full_name = String()

    @staticmethod
    def resolve_full_name(user: User, *_):
        return user.get_full_name()
