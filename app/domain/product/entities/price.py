class WholesaleEntity:
    def __init__(
            self,
            id_: int | None,
            wholesale: float | None = None,
            status: bool = False
    ):
        self.id_ = id_
        self.wholesale = wholesale
        self.status = status


class PriceEntity:
    def __init__(
            self,
            id_: int | None,
            wholesale: list[WholesaleEntity] | None = None,
            retail: float | None = None,
    ):
        self.id_ = id_
        self.wholesale = wholesale
        self.retail = retail
