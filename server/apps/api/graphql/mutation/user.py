import graphene

from apps.api.graphql.utils.decorators import is_authenticated


class DeleteUserMutation(graphene.Mutation):

    message = graphene.String()

    @is_authenticated(raise_exception=True)
    def mutate(self, info):
        info.context.user.is_active = False
        info.context.user.save()
        return DeleteUserMutation(message="User deleted")
