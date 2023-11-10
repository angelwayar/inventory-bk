from typing import Sequence

from sqlalchemy import select, update
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from app.domain.product.entities.product import ProductEntity
from app.domain.product.repositories.product_repository import ProductRepository
from app.infrastructure.product.models.product import Product


class ProductRepositoryImpl(ProductRepository):

    def __init__(self, session: Session):
        self.session: Session = session

    def massively_create(self, products: Sequence[ProductEntity]):
        pass

    def create(self, entity: ProductEntity) -> ProductEntity:
        product = Product.from_entity(entity)

        self.session.add(product)

        return product.to_entity()

    def find_all(self) -> Sequence[ProductEntity]:
        statement = select(Product)
        try:
            result: Sequence[Product] = self.session.execute(statement).scalar().all()
        except NoResultFound:
            return []

        return [product.to_entity() for product in result]

    def find_by_id(self, id_: int) -> ProductEntity | None:
        result: Product | None = self.session.get(Product, id_)

        if result is None:
            return None

        return result.to_entity()

    def update(self, entity: ProductEntity) -> ProductEntity:
        product = Product.from_entity(entity)
        update_data = product.to_dict()

        statement = update(Product).filter_by(id_=product.id_).values(update_data).returning(Product)

        product_mapping: Product | None = self.session.execute(statement=statement).fetchone()

        if product_mapping is None:
            raise
        result, = product_mapping

        return result.to_entity()

    def delete_by_id(self, id_: int) -> ProductEntity:
        product: Product | None = self.session.get(Product, id_)

        if product is not None:
            self.session.delete(product)
            self.session.flush()

            return product.to_entity()

        raise
