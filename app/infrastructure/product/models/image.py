from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.core.models.base_model import Base


class Image(Base):
    __tablename__ = "images"

    product_id: Mapped[int] = mapped_column(ForeignKey("products.id_"))
    image: Mapped[str] = Column(String, nullable=True)
