class ImageEntity:
    def __init__(
            self,
            id_: int | None,
            product_id: int,
            image: str # Averiguar bien el tipo de imagen a guardar base64
    ):
        self.id_ = id_
        self.product_id = product_id
        self.image = image
