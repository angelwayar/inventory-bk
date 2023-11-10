from pydantic import Field, BaseModel


class ImageCreateModel(BaseModel):
    image: str | None = Field(example='image.jpg')
