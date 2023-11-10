from abc import abstractmethod
from typing import Sequence

from app.core.repositories.base_repository import BaseRepository
from app.domain.product.entities.product import ProductEntity


# Verificar si se debe de enviar una lista de Productos
class ProductRepository(BaseRepository[ProductEntity]):
    @abstractmethod
    def massively_create(self, products: Sequence[ProductEntity]):
        raise NotImplementedError()
