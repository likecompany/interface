from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from likeinterface.methods.base import Method, Request
from likeinterface.types import Balance

if TYPE_CHECKING:
    from likeinterface.interface import Interface


class GetBalanceMethod(Method[Balance]):
    """
    Use this method to get balance for user.

    Parameters
      Name            | Type    | Required | Description

      1. user_id      | Integer | Yes      | User ID in the system. Send user_id=0 for get current user balance and provide access_token parameter.
      2. access_token | String  | No       | Auth access token

    Result
      :class:`likeinterface.types.balance.balance.Balance`
    """

    __name__ = "balance.getBalance"
    __returning__ = Balance

    user_id: int
    access_token: Optional[str] = None

    def request(self, interface: Interface) -> Request:
        return Request(method=self.__name__, data=self.model_dump())