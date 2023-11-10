from abc import abstractmethod
from typing import Sequence

from app.core.use_case.base_use_case import BaseUseCase
from app.domain.product.results.product_query_model import ProductReadModel
from app.domain.product.services.product_query_service import ProductQueryService


class GetProductsUseCase(BaseUseCase[None, Sequence[ProductReadModel]]):
    service: ProductQueryService

    @abstractmethod
    def __call__(self, args: None) -> Sequence[ProductReadModel]:
        raise NotImplementedError()


class GetProductsUseCaseImpl(GetProductsUseCase):

    def __init__(self, service: ProductQueryService):
        self.service: ProductQueryService = service

    def __call__(self, args: None) -> Sequence[ProductReadModel]:
        try:
            products = self.service.find_all()
        except Exception as _e:
            raise

        return products
