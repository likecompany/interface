from __future__ import annotations

from typing import Any

from pydantic.dataclasses import dataclass


@dataclass
class Network:
    """
    Class describing access to different services.
    """

    base: str

    def url(self, **kwargs: Any) -> str:
        """
        Formats base url for request.

        :param kwargs: format kwargs
        :return: url
        """

        return self.base.format(**kwargs)