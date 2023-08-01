from __future__ import annotations

from typing import TYPE_CHECKING

from likeinterface.methods.base import Method, Request

if TYPE_CHECKING:
    from likeinterface.interface import Interface


class SignInMethod(Method[bool]):
    """
    Use this method to sign in a user with a validated email address

    Parameters
      Name               | Type   | Required | Description

      1. email           | String | Yes      | Email address
      2. code            | String | Yes      | Verification code
      3. email_code_hash | String | Yes      | Email message ID

    Result
      :class:`bool`
    """

    __name__ = "/auth.signIn"
    __returning__ = bool

    email: str
    code: str
    email_code_hash: str

    def request(self, interface: Interface) -> Request:
        return Request(method=self.__name__, data=self.model_dump())
