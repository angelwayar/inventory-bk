from pydantic import BaseModel, Field

from app.domain.product.entities.product import ProductEntity
from app.domain.product.results.detail_query_model import DetailReadModel
from app.domain.product.results.image_query_model import ImageReadModel
from app.domain.product.results.price_query_model import PriceReadModel


class ProductReadModel(BaseModel):
    id_: int = Field(example=1)
    code: str | None = Field(example=1),
    detail: DetailReadModel | None
    price: PriceReadModel | None
    images: list[ImageReadModel] | None

    class Config:
        from_attributes = True

    @staticmethod
    def from_entity(entity: ProductEntity) -> 'ProductReadModel':
        return ProductReadModel(
            id_=entity.id_,
            code=entity.code,
            detail=DetailReadModel.from_entity(entity.detail),
            price=PriceReadModel.from_entity(entity.price),
            images=[ImageReadModel.from_entity(image) for image in entity.images]
        )
