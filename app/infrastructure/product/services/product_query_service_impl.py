from typing import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.domain.product.results.product_query_model import ProductReadModel
from app.domain.product.services.product_query_service import ProductQueryService
from app.infrastructure.product.models.product import Product


class ProductQueryServiceImpl(ProductQueryService):
    def __init__(self, session: Session):
        self.session: Session = session

    def find_by_id(self, id_: int) -> ProductReadModel | None:
        result: Product | None = self.session.get(Product, id_)

        if result is None:
            return None

        return result.to_read_model()

    def find_all(self) -> Sequence[ProductReadModel]:
        statement = select(Product)
        result: Sequence[Product] | None = self.session.execute(statement=statement).scalars().all()

        return [product.to_read_model() for product in result]
