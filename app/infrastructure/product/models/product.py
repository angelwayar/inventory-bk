from typing import List

from sqlalchemy import Column, String, Boolean, ForeignKey, Integer
from sqlalchemy.orm import Mapped, relationship

from app.core.models.base_model import Base
from app.domain.product.entities.product import ProductEntity
from app.domain.product.results.product_query_model import ProductReadModel
from app.infrastructure.product.models.detail import Detail
from app.infrastructure.product.models.image import Image
from app.infrastructure.product.models.price import Price
from app.infrastructure.supplier.models.supplier import Supplier


class Product(Base):
    __tablename__ = "products"

    supplier_id: Mapped[int] = Column(Integer, ForeignKey("suppliers.id_"), nullable=True)
    supplier: Mapped["Supplier"] = relationship(back_populates='products')

    images: Mapped[List["Image"] | None] = relationship(back_populates='product_image', cascade="all, delete-orphan")
    code: Mapped[str] = Column(String, unique=True, index=True, nullable=True)
    detail: Mapped["Detail"] = relationship(back_populates='product_detail', cascade="all, delete-orphan")
    price: Mapped["Price"] = relationship(back_populates='product_price', cascade="all, delete-orphan")
    relationship: Mapped[bool] = Column(Boolean, default=False)

    def to_entity(self) -> ProductEntity:
        return ProductEntity(
            id_=self.id_,
            code=self.code,
            detail=self.detail.to_entity(),
            price=self.price.to_entity(),
            images=[image.to_entity() for image in self.images]
        )

    def to_dict(self):
        return {
            'id_': self.id_,
            'code': self.code,
            'detail': self.detail.to_dict(),
            'price': self.price.to_dict(),
            'images': [image.to_dict() for image in self.images]
        }

    def to_read_model(self) -> ProductReadModel:
        return ProductReadModel(
            id_=self.id_,
            code=self.code,
            detail=self.detail.to_read_model(),
            price=self.price.to_read_model(),
            images=[image.to_read_model() for image in self.images]
        )

    @staticmethod
    def from_entity(product: ProductEntity) -> 'Product':
        return Product(
            id_=product.id_,
            code=product.code,
            detail=Detail.from_entity(product.detail),
            price=Price.from_entity(product.price),
            images=[Image.from_entity(image) for image in product.images]
        )
