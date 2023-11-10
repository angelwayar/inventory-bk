from app.core.unitOfWork.base_unit_of_work import AbstractUnitOfWork
from app.domain.product.repositories.product_repository import ProductEntity


class ProductUnitOfWork(AbstractUnitOfWork[ProductEntity]):
    pass
