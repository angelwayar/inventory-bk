from app.core.errors.base_exception import BaseError


class ProductNotFoundError(BaseError):
    message = 'Product does not exist.'


class ProductsNotFoundError(BaseError):
    message = 'Products does not exist.'


class ProductAlreadyExistsError(BaseError):
    message = 'Product already exists.'
