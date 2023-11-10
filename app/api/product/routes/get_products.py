from fastapi import Depends, HTTPException, status

from app.api.product.routes import router
from app.api.product.schemas.product_error_message import ErrorMessageProductNotFound
from app.domain.product.dependencies import get_products_use_case
from app.domain.product.use_cases.get_products import GetProductsUseCase


@router.get(
    '/',
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            'model': ErrorMessageProductNotFound
        }
    }
)
def get_products(
        get_products_use_case_: GetProductsUseCase = Depends(get_products_use_case)
):
    try:
        products = get_products_use_case_(None)
    except Exception as _e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    if not products:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )

    return products
