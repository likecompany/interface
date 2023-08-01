from __future__ import annotations

from typing import TYPE_CHECKING

from likeinterface.methods.base import Method, Request
from likeinterface.types import SendCode

if TYPE_CHECKING:
    from likeinterface.interface import Interface


class SendCodeMethod(Method[SendCode]):
    """
    Use this method to send the verification code for login.

    Parameters
      Name     | Type   | Required | Description

      1. email | String | Yes      | Email address

    Result
      :class:`likeinterface.types.auth.send_code.SendCode`
    """

    __name__ = "/auth.sendCode"
    __returning__ = SendCode

    email: str

    def request(self, interface: Interface) -> Request:
        return Request(method=self.__name__, data=self.model_dump())
