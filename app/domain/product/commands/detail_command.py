from pydantic import Field, BaseModel


class DetailCreateModel(BaseModel):
    description: str | None = Field(example='COROLLA'),
    part: str | None = Field(example='2-L'),
    width: float | None = Field(example='68'),
    height: float | None = Field(example='33'),
    depth: float | None = Field(example='26'),
    age: str | None = Field(example='90')
