from typing import List

from sqlalchemy import Column, Integer, Float, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, relationship

from app.core.models.base_model import Base
from app.domain.product.entities.price import PriceEntity, WholesaleEntity
from app.domain.product.results.price_query_model import WholesaleReadModel, PriceReadModel


class Wholesale(Base):
    __tablename__ = 'wholesale_prices'

    wholesale: Mapped[float | None] = Column(Float, nullable=True)
    status: Mapped[bool] = Column(Boolean, default=False)

    price_id: Mapped[int] = Column(Integer, ForeignKey("prices.id_", ondelete="CASCADE"))
    price: Mapped['Price'] = relationship(back_populates='wholesale_prices')

    def to_entity(self) -> WholesaleEntity:
        return WholesaleEntity(
            id_=self.id_,
            wholesale=self.wholesale,
            status=self.status
        )

    def to_dict(self):
        return {
            'id_': self.id_,
            'wholesale': self.wholesale,
            'status': self.status
        }

    def to_read_model(self) -> WholesaleReadModel:
        return WholesaleReadModel(
            id_=self.id_,
            wholesale=self.wholesale,
            status=self.status
        )

    @staticmethod
    def from_entity(wholesale: WholesaleEntity) -> 'Wholesale':
        return Wholesale(
            id_=wholesale.id_,
            wholesale=wholesale.wholesale,
            status=wholesale.status,
        )


class Price(Base):
    __tablename__ = 'prices'

    retail: Mapped[float | None] = Column(Float, nullable=True)

    wholesale_prices: Mapped[List['Wholesale'] | None] = relationship(
        back_populates='price',
        cascade="all, delete-orphan"
    )

    product_id: Mapped[int] = Column(Integer, ForeignKey("products.id_", ondelete="CASCADE"))
    product_price: Mapped['Product'] = relationship(back_populates="price")

    def to_entity(self) -> PriceEntity:
        return PriceEntity(
            id_=self.id_,
            wholesale=[wholesale.to_entity() for wholesale in self.wholesale_prices],
            retail=self.retail,
        )

    def to_dict(self):
        return {
            'id_': self.id_,
            'wholesale_prices': [wholesale.to_dict() for wholesale in self.wholesale_prices],
            'retail': self.retail,
        }

    def to_read_model(self) -> PriceReadModel:
        return PriceReadModel(
            id_=self.id_,
            retail=self.retail,
            wholesale_prices=[wholesale.to_read_model() for wholesale in self.wholesale_prices],
        )

    @staticmethod
    def from_entity(price: PriceEntity) -> 'Price':
        return Price(
            id_=price.id_,
            wholesale_prices=[Wholesale.from_entity(wholesale_data) for wholesale_data in price.wholesale],
            retail=price.retail,
        )
