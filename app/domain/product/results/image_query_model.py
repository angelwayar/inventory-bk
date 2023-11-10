from pydantic import BaseModel,Field

from app.domain.product.entities.image import ImageEntity


class ImageReadModel(BaseModel):
    id_: int = Field(example=1)
    image: str | None = Field(example='image.jpg')

    class Config:
        from_attributes = True

    @staticmethod
    def from_entity(entity: ImageEntity) -> 'ImageReadModel':
        return ImageReadModel(
            id_=entity.id_,
            image=entity.image_path
        )
