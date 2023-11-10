from pydantic import BaseModel, Field

from app.domain.product.entities.price import PriceEntity, WholesaleEntity


class WholesaleReadModel(BaseModel):
    id_: int = Field(example=1)
    wholesale: float | None = Field(example=1)
    status: bool = Field(example=1, default=False)

    class Config:
        from_attributes = True

    @staticmethod
    def from_entity(entity: WholesaleEntity) -> 'WholesaleReadModel':
        return WholesaleReadModel(
            id_=entity.id_,
            wholesale=entity.wholesale,
            status=entity.status
        )


class PriceReadModel(BaseModel):
    id_: int = Field(example=1)
    retail: float | None = Field(example=310.0)
    wholesale_prices: list[WholesaleReadModel] | None

    class Config:
        from_attributes = True

    @staticmethod
    def from_entity(entity: PriceEntity) -> 'PriceReadModel':
        return PriceReadModel(
            id_=entity.id_,
            retail=entity.retail,
            wholesale_prices=[WholesaleReadModel.from_entity(wholesale) for wholesale in entity.wholesale]
        )
