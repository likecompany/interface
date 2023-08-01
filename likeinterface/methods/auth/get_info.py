from __future__ import annotations

from typing import TYPE_CHECKING

from likeinterface.methods.base import Method, Request
from likeinterface.types import User

if TYPE_CHECKING:
    from likeinterface.interface import Interface


class GetInfoMethod(Method[User]):
    """
    Use this method to get information about user.

    Parameters
      This constructor does not require any parameters.

    Result
      :class:`likeinterface.types.auth.user.User`
    """

    __name__ = "/auth.getInfo"
    __returning__ = User

    def request(self, interface: Interface) -> Request:
        return Request(method=self.__name__, data=self.model_dump())
