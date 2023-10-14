from datetime import datetime

from sqlalchemy import Column, Integer, Float, String, DATE, ForeignKey
from sqlalchemy.orm import Mapped, relationship

from app.core.models.base_model import Base
from app.domain.product.entities.description import DescriptionEntity


class Description(Base):
    __tablename__ = "descriptions"

    detail: Mapped[str | None] = Column(String, nullable=True)
    width: Mapped[float | None] = Column(Float, nullable=True)
    height: Mapped[float | None] = Column(Float, nullable=True)
    age: Mapped[datetime | None] = Column(DATE, nullable=True)

    product_id: Mapped[int] = Column(Integer, ForeignKey("products.id_"))
    product: Mapped["Product"] = relationship(back_populates="description")

    def to_entity(self) -> DescriptionEntity:
        return DescriptionEntity(
            id_=self.id_,
            detail=self.detail,
            width=self.width,
            height=self.height,
            age=self.age
        )

    @staticmethod
    def from_entity(description: DescriptionEntity) -> 'Description':
        return Description(
            id_=description.id_,
            detail=description.detail,
            width=description.width,
            height=description.height,
            age=description.age
        )
