from __future__ import annotations

import datetime as dt
from typing import Optional

from likeinterface.types.base import LikeObject


class User(LikeObject):
    id: int
    """User id in the system."""
    email: str
    """Validated user email address."""
    datetime: dt.datetime
    """Registration date."""
    updated_at: Optional[dt.datetime] = None
    """Last change information date"""
    first_name: str
    """User first name."""
    last_name: Optional[str] = None
    """User second name."""
    full_name: str
    """User First name and second name"""
