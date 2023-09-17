from description import DescriptionEntity
from image import ImageEntity
from price import PriceEntity


class ProductEntity:
    def __init__(
            self,
            code: str,
            detail: DescriptionEntity,
            price: PriceEntity,
            images: ImageEntity,
            # Quizas haya que agregar la entidad de relacion para poder visualizarlas en la lista

            relationship: bool = False
    ):
        self.code = code
        self.detail = detail
        self.price = price
        self.images = images
        self.relationship = relationship
