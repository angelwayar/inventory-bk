class PriceEntity:
    def __init__(
            self,
            id_: int | None,
            wholesale: float | None,
            retail: float | None,
            privileged: float
    ):
        self.id_ = id_
        self.wholesale = wholesale
        self.retail = retail
        self.privileged = privileged
