class ImageEntity:
    def __init__(
            self,
            id_: int | None,
            image_path: str | None = None  # Averiguar bien el tipo de imagen a guardar base64
    ):
        self.id_ = id_
        self.image_path = image_path
