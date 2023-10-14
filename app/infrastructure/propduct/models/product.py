from typing import List

from sqlalchemy import Column, String, Boolean, ForeignKey, Integer
from sqlalchemy.orm import Mapped, relationship

from app.core.models.base_model import Base
# from app.domain.product.entities.product import ProductEntity
from app.infrastructure.propduct.models.image import Image


class Product(Base):
    __tablename__ = "products"

    supplier_id: Mapped[int] = Column(Integer, ForeignKey("suppliers.id_"), nullable=False)
    image: Mapped[List["Image"]] = relationship()
    code: Mapped[str] = Column(String, unique=True, index=True, nullable=False)
    description: Mapped["Description"] = relationship(back_populates="product")
    price: Mapped["Price"] = relationship(back_populates="product")
    relationship: Mapped[bool] = Column(Boolean, default=False)

    # @staticmethod
    # def from_entity(product: ProductEntity) -> 'Product':
    #     return Product(
    #         id_=product.id_
    #     )
