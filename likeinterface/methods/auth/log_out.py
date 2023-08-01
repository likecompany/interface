from __future__ import annotations

from typing import TYPE_CHECKING

from likeinterface.methods.base import Method, Request

if TYPE_CHECKING:
    from likeinterface.interface import Interface


class LogOutMethod(Method[bool]):
    """
    Use this method to log out the user.

    Parameters
      This constructor does not require any parameters.

    Result
      :class:`bool`
    """

    __name__ = "/auth.logOut"
    __returning__ = bool

    def request(self, interface: Interface) -> Request:
        return Request(method=self.__name__, data=self.model_dump())
