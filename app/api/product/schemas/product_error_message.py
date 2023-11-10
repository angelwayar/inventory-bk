from pydantic import BaseModel, Field

from app.core.errors.product_exception import ProductNotFoundError, ProductAlreadyExistsError, ProductsNotFoundError


class ErrorMessageProductNotFound(BaseModel):
    detail: str = Field(example=ProductNotFoundError.message)


class ErrorMessageProductsNotFound(BaseModel):
    detail: str = Field(example=ProductsNotFoundError.message)


class ErrorMessageProductAlreadyExists(BaseModel):
    detail: str = Field(example=ProductAlreadyExistsError.message)
