class RelationshipEntity:
    def __init__(
            self,
            id_: int | None,
            product_id: int,
            substitute_product_id: int
    ):
        self.id_ = id_
        self.product_id = product_id
        self.substitute_product_id = substitute_product_id
