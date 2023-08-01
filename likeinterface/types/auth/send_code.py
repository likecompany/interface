from __future__ import annotations

from starlette.requests import Request

from likeinterface.types.base import LikeObject


class SendCode(LikeObject):
    email_code_hash: str
    """Email message ID."""
    request: Request
