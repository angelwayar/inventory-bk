import json

from pydantic import BaseModel, Field, model_validator

from app.domain.product.commands.detail_command import DetailCreateModel
from app.domain.product.commands.image_command import ImageCreateModel
from app.domain.product.commands.price_command import PriceCreateModel


class ProductCreateModel(BaseModel):
    code: str | None = Field(example='TO-0047')
    detail: DetailCreateModel | None
    price: PriceCreateModel | None
    images: list[ImageCreateModel] | None

    @model_validator(mode='before')
    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value


class ProductUpdateModel(BaseModel):
    id_: int
    code: str | None = Field(example='TO-0047')
    detail: DetailCreateModel | None
    price: PriceCreateModel | None
    images: list[ImageCreateModel] | None
