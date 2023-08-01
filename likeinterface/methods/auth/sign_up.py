from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from likeinterface.methods.base import Method, Request
from likeinterface.types import User

if TYPE_CHECKING:
    from likeinterface.interface import Interface


class SignUpMethod(Method[User]):
    """
    Use this method to register a validated email in the system.

    Parameters
      Name               | Type   | Required | Description

      1. email           | String | Yes      | Email address
      2. email_code_hash | String | Yes      | Email message ID
      3. first_name      | String | Yes      | New user first name
      4. second_name     | String | No       | New user second name

    Result
      :class:`likeinterface.types.auth.user.User`
    """

    __name__ = "/auth.signUp"
    __returning__ = User

    email: str
    email_code_hash: str
    first_name: str
    second_name: Optional[str] = None

    def request(self, interface: Interface) -> Request:
        return Request(method=self.__name__, data=self.model_dump())
