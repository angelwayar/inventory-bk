from abc import abstractmethod
from typing import Tuple

from app.core.errors.product_exception import ProductNotFoundError
from app.core.use_case.base_use_case import BaseUseCase
from app.domain.product.results.product_query_model import ProductReadModel
from app.domain.product.services.product_query_service import ProductQueryService


class GetProductUseCase(BaseUseCase[Tuple[int], ProductReadModel]):
    service: ProductQueryService

    @abstractmethod
    def __call__(self, args: Tuple[int]) -> ProductReadModel:
        raise NotImplementedError()


class GetProductUseCaseImpl(GetProductUseCase):

    def __init__(self, service: ProductQueryService):
        self.service: ProductQueryService = service

    def __call__(self, args: Tuple[int]) -> ProductReadModel:
        id_, = args

        try:
            product = self.service.find_by_id(id_)
            if product is None:
                raise ProductNotFoundError()
        except Exception:
            raise

        return product
