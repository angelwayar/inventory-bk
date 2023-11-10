import copy
import sys
from typing import Any, Callable

sys.path.append("..")
from app.domain.product.entities.detail import DetailEntity
from app.domain.product.entities.image import ImageEntity
from app.domain.product.entities.price import PriceEntity
from app.domain.product.commands.product_command import ProductCreateModel


class ProductEntity:
    def __init__(
            self,
            id_: int | None,
            code: str | None,
            detail: DetailEntity | None,
            price: PriceEntity | None,
            images: list[ImageEntity] | None = None,
            relationship: bool = False
    ):
        self.id_ = id_
        self.code = code
        self.detail = detail
        self.price = price
        self.images = images
        self.relationship = relationship

    def update_entity(
            self,
            entity_update_model: 'ProductCreateModel',
            get_update_data_fn: Callable[['ProductCreateModel'], dict[str, Any]]
    ) -> 'ProductEntity':
        update_data = get_update_data_fn(entity_update_model)
        update_entity = copy.deepcopy(self)
        algo = dict({
            'id_': update_entity.id_,
            'code': update_entity.code,
            'detail': update_entity.detail
        }
        )

        for attr_name, value in update_data.items():
            print(attr_name)
            if attr_name == 'detail':
                value.update({'id_': update_entity.detail.id_})
                update_entity.detail.__setattr__(attr_name, value)
            if attr_name == 'price':
                value.update({'id_': update_entity.price.id_})
                for data in [update_entity.price.wholesale, value['wholesale']]:
                    for wholesale_udpated in value['wholesale']:
                        pass

                    # print(data)
                    # print(wholesale_updated)
                    # wholesale_updated.update({'id_': wholesale_entity.id_})
                print(value)
            # if attr_name == 'image':
            else:
                update_entity.__setattr__(attr_name, value)

        return update_entity

    def __eq__(self, other: object) -> bool:
        if isinstance(other, ProductEntity):
            return self.id_ == other.id_

        return False

    def to_popo(self) -> object:
        return self.__dict__
