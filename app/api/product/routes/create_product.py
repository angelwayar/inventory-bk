from typing import List

from fastapi import Depends, HTTPException, status, Response, Request, File, UploadFile, Body

from app.api.product.routes import router
from app.api.product.schemas.product_error_message import ErrorMessageProductAlreadyExists
from app.domain.product.commands.product_command import ProductCreateModel
from app.domain.product.dependencies import get_create_product_use_case
from app.domain.product.use_cases.create_product import CreateProductUseCase


@router.post(
    '/',
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_409_CONFLICT: {
            'model': ErrorMessageProductAlreadyExists
        }
    }
)
def create_product(
        response: Response,
        request: Request,
        data: ProductCreateModel = Body(...),
        files: List[UploadFile] = File(...),
        create_product_use_case: CreateProductUseCase = Depends(get_create_product_use_case),
):
    try:
        product = create_product_use_case((data, files))
    except Exception as _exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    return product
