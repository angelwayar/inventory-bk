from app.core.services.base_query_service import QueryService
from app.domain.product.results.product_query_model import ProductReadModel


class ProductQueryService(QueryService[ProductReadModel]):
    pass
