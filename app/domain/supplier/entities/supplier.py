from app.domain.product.entities.product import ProductEntity


class SupplierEntity:
    def __init__(
            self,
            id_: int | None,
            name: str | None = None,
            products: list[ProductEntity] | None = None,
    ):
        self.id_ = id_
        self.name = name
        self.products = products
