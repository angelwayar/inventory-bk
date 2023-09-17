from datetime import datetime


class DescriptionEntity:
    def __init__(
            self,
            id_: int | None,
            detail: str | None,
            width: float | None,
            height: float | None,
            age: datetime | None
    ):
        self.id_ = id_
        self.detail = detail
        self.width = width
        self.height = height
        self.age = age
