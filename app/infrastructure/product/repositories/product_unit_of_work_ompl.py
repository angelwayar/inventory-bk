from sqlalchemy.orm import Session

from app.domain.product.repositories.product_repository import ProductRepository
from app.domain.product.repositories.product_unit_of_work import ProductUnitOfWork


class ProductUnitOfWorkImpl(ProductUnitOfWork):
    def __init__(
            self,
            session: Session,
            product_repository: ProductRepository
    ):
        self.session: Session = session
        self.repository: ProductRepository = product_repository

    def begin(self):
        self.session.begin()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
