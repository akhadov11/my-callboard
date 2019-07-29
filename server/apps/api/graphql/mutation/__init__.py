from apps.api.graphql.mutation.user import DeleteUserMutation


class UserMutation(object):
    delete_current_user = DeleteUserMutation.Field()
