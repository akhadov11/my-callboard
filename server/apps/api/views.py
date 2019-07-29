import time

from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from graphene_django.views import GraphQLView as OriginalGraphQLView


class GraphQLView(OriginalGraphQLView):
    @staticmethod
    def format_error(error):
        res_error = OriginalGraphQLView.format_error(error)
        if "locations" in res_error:
            del res_error["locations"]
        if hasattr(error, "original_error"):
            res_error["type"] = error.original_error.__class__.__name__
        return res_error


class Ping(APIView):
    permission_classes = (AllowAny,)

    def get(self, _):
        return Response({"response": "pong", "timestamp": time.time()})
