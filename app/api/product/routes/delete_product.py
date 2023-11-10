from fastapi import Depends, HTTPException, status

from app.api.product.routes import router
from app.api.product.schemas.product_error_message import ErrorMessageProductNotFound
from app.core.errors.product_exception import ProductNotFoundError
from app.domain.product.dependencies import get_delete_product_use_case
from app.domain.product.results.product_query_model import ProductReadModel
from app.domain.product.use_cases.delete_product import DeleteProductUseCase


@router.delete(
    '/{id_}/',
    response_model=ProductReadModel,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            'model': ErrorMessageProductNotFound
        }
    }
)
def delete_product(
        id_: int,
        delete_product_use_case: DeleteProductUseCase = Depends(get_delete_product_use_case)
):
    try:
        product = delete_product_use_case((id_,))
    except ProductNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    except Exception as _e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return product
