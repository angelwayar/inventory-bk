from pydantic import Field, BaseModel


class WholesaleCreateModel(BaseModel):
    wholesale: float | None = Field(example='310', default=None)
    status: bool = Field(example='True', default=False)


class PriceCreateModel(BaseModel):
    wholesale: list[WholesaleCreateModel] | None = Field(default=[]),
    retail: float | None = Field(example='420', default=None),
