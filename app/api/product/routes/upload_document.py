from fastapi import UploadFile, Depends, HTTPException, status

from app.api.product.routes import router
from app.domain.product.dependencies import get_massively_create_use_case
from app.domain.product.use_cases.massively_create import MassivelyCreateUseCase


@router.post('/document')
def upload_products(
        file: UploadFile,
        massively_create_use_case: MassivelyCreateUseCase = Depends(get_massively_create_use_case)
):
    try:
        algo = massively_create_use_case((file,))
    except Exception as _exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    return algo
