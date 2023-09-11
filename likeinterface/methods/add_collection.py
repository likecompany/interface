from __future__ import annotations

from typing import TYPE_CHECKING, List

from likeinterface.methods.base import Method
from likeinterface.types import CollectionElement, File

if TYPE_CHECKING:
    from likeinterface.interface import Interface


class AddCollection(Method[File]):
    """
    Use this method to add new card collection.

    Parameters
      Name                   | Type                       | Required | Description

      1. access_token        | String                     | Yes      | Auth access token
      2. name                | String                     | Yes      | Collection name
      3. collection_elements | Array Of CollectionElement | Yes      | Collection set, requires all cards from Two Clubs to Ace Spades

    Result
      :class:`likeinteface.types.collection.Collection`
    """

    __is_form__ = True
    __name__ = "collection.addCollection"
    __returning__ = File

    access_token: str
    name: str
    collection_elements: List[CollectionElement]

    def request(self, interface: Interface) -> None:
        return None