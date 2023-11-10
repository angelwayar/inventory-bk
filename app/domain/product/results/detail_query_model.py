from pydantic import BaseModel,Field

from app.domain.product.entities.detail import DetailEntity


class DetailReadModel(BaseModel):
    id_: int = Field(example=1)
    description: str | None = Field(example='COROLLA')
    part: str | None = Field(example='')
    width: float | None = Field(example='')
    height: float | None = Field(example='')
    depth: float | None = Field(example='')
    age: str | None = Field(example='')

    class Config:
        from_attributes = True

    @staticmethod
    def from_entity(entity: DetailEntity) -> 'DetailReadModel':
        return DetailReadModel(
            id_=entity.id_,
            description=entity.description,
            part=entity.part,
            width=entity.width,
            height=entity.height,
            depth=entity.depth,
            age=entity.age
        )
