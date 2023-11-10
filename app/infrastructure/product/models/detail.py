from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import Mapped, relationship

from app.core.models.base_model import Base
from app.domain.product.entities.detail import DetailEntity
from app.domain.product.results.detail_query_model import DetailReadModel


class Detail(Base):
    __tablename__ = "details"

    description: Mapped[str | None] = Column(String, nullable=True)
    part: Mapped[str | None] = Column(String, nullable=True)
    width: Mapped[float | None] = Column(Float, nullable=True)
    height: Mapped[float | None] = Column(Float, nullable=True)
    depth: Mapped[float | None] = Column(Float, nullable=True)
    age: Mapped[str | None] = Column(String, nullable=True)

    product_id: Mapped[int] = Column(Integer, ForeignKey("products.id_", ondelete="CASCADE"))
    product_detail: Mapped["Product"] = relationship(back_populates="detail")

    def to_entity(self) -> DetailEntity:
        return DetailEntity(
            id_=self.id_,
            description=self.description,
            part=self.part,
            width=self.width,
            height=self.height,
            depth=self.depth,
            age=self.age
        )

    def to_dict(self):
        return {
            'id_': self.id_,
            'description': self.description,
            'part': self.part,
            'width': self.width,
            'height': self.height,
            'depth': self.depth,
            'age': self.age
        }

    def to_read_model(self) -> DetailReadModel:
        return DetailReadModel(
            id_=self.id_,
            description=self.description,
            part=self.part,
            width=self.width,
            height=self.height,
            depth=self.depth,
            age=self.age
        )

    @staticmethod
    def from_entity(detail: DetailEntity) -> 'Detail':
        return Detail(
            id_=detail.id_,
            description=detail.description,
            part=detail.part,
            width=detail.width,
            height=detail.height,
            depth=detail.depth,
            age=detail.age
        )
