from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional, Union, Dict, Any

from django.http import HttpRequest, HttpResponse


if TYPE_CHECKING:
    from .consumer import GraphQLWSConsumer


@dataclass
class GraphQLChannelsContext:
    """
    A Channels context for GraphQL
    """

    request: Optional[Union[HttpRequest, "GraphQLWSConsumer"]]
    response: Optional[HttpResponse]
    scope: Optional[Dict[str, Any]]

    @property
    def ws(self):
        return self.request

    def __getitem__(self, key):
        # __getitem__ override needed to avoid issues for who's
        # using info.context["request"]
        return super().__getattribute__(key)

    def get(self, key):
        """Enable .get notation for accessing the request"""
        return super().__getattribute__(key)

    @property
    def user(self):
        return self.scope["user"]