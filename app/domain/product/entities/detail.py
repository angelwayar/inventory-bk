import copy
from typing import Any, Callable

from app.domain.product.commands.detail_command import DetailCreateModel


class DetailEntity:
    def __init__(
            self,
            id_: int | None,
            description: str | None = None,
            part: str | None = None,
            width: float | None = None,
            height: float | None = None,
            depth: float | None = None,
            age: str | None = None
    ):
        self.id_ = id_
        self.description = description
        self.part = part
        self.width = width
        self.height = height
        self.depth = depth
        self.age = age

    def update_entity(
            self,
            entity_update_model: 'DetailCreateModel',
            get_update_data_fn: Callable[['DetailCreateModel'], dict[str, Any]]
    ) -> 'DetailEntity':
        update_data = get_update_data_fn(entity_update_model)
        update_entity = copy.deepcopy(self)

        for attr_name, value in update_data.items():
            update_entity.__setattr__(attr_name, value)

        return update_entity

    def __eq__(self, other: object) -> bool:
        if isinstance(other, DetailEntity):
            return self.id_ == other.id_

        return False

    def to_popo(self) -> object:
        return self.__dict__
