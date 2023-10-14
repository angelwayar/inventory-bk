from typing import List

from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped, relationship

from app.core.models.base_model import Base
from app.domain.supplier.entities.supplier import SupplierEntity


class Supplier(Base):
    __tablename__ = "suppliers"

    name: Mapped[str] = Column(String)
    product: Mapped[List["Product"]] = relationship()

    # def to_entity(self) -> :

    @staticmethod
    def from_entity(supplier: SupplierEntity) -> 'Supplier':
        return Supplier(
            id_=supplier.id_,
            name=supplier.name
        )
