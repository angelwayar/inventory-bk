from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import Mapped, relationship

from app.core.models.base_model import Base
from app.domain.product.entities.price import PriceEntity


class Price(Base):
    __tablename__ = 'prices'

    wholesale: Mapped[float | None] = Column(Float, nullable=True)
    retail: Mapped[float | None] = Column(Float, nullable=True)
    privileged: Mapped[float] = Column(Float, nullable=False)

    product_id: Mapped[int] = Column(Integer, ForeignKey("products.id_"))
    product: Mapped["Product"] = relationship(back_populates="price")

    def to_entity(self) -> PriceEntity:
        return PriceEntity(
            id_=self.id_,
            wholesale=self.wholesale,
            retail=self.retail,
            privileged=self.privileged
        )

    @staticmethod
    def from_entity(price: PriceEntity) -> 'Price':
        return Price(
            id_=price.id_,
            wholesale=price.wholesale,
            retail=price.retail,
            privileged=price.privileged
        )
