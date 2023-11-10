from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import Mapped, relationship, backref

from app.core.models.base_model import Base
from app.domain.product.entities.image import ImageEntity
from app.domain.product.results.image_query_model import ImageReadModel


class Image(Base):
    __tablename__ = "images"

    image_path: Mapped[str | None] = Column(String, nullable=True)

    product_id: Mapped[int] = Column(Integer, ForeignKey("products.id_", ondelete="CASCADE"))
    product_image: Mapped["Product"] = relationship(back_populates="images")

    def to_entity(self) -> ImageEntity:
        return ImageEntity(
            id_=self.id_,
            image_path=self.image_path
        )

    def to_dict(self):
        return {
            'id_': self.id_,
            'image_path': self.image_path
        }

    def to_read_model(self) -> ImageReadModel:
        return ImageReadModel(
            id_=self.id_,
            image=self.image_path
        )

    @staticmethod
    def from_entity(image: ImageEntity) -> 'Image':
        return Image(
            id_=image.id_,
            image_path=image.image_path
        )
