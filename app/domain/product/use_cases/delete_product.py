from abc import abstractmethod
from typing import Tuple

from app.core.errors.product_exception import ProductNotFoundError
from app.core.use_case.base_use_case import BaseUseCase
from app.domain.product.repositories.product_unit_of_work import ProductUnitOfWork
from app.domain.product.results.product_query_model import ProductReadModel


class DeleteProductUseCase(BaseUseCase):
    unit_of_work: ProductUnitOfWork

    @abstractmethod
    def __call__(self, args: Tuple[int]) -> ProductReadModel:
        raise NotImplementedError()


class DeleteProductUseCaseImpl(DeleteProductUseCase):
    def __init__(self, unit_of_work: ProductUnitOfWork):
        self.unit_of_work: ProductUnitOfWork = unit_of_work

    def __call__(self, args: Tuple[int]) -> ProductReadModel:
        id_, = args
        existing_product = self.unit_of_work.repository.find_by_id(id_)

        if existing_product is None:
            raise ProductNotFoundError()

        try:
            delete_product = self.unit_of_work.repository.delete_by_id(id_)
        except Exception as e:
            self.unit_of_work.rollback()
            raise

        self.unit_of_work.commit()

        return ProductReadModel.from_entity(delete_product)
