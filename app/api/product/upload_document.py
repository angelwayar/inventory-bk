from fastapi import UploadFile
from app.api.product import router


@router.post('/document')
def upload_products(file: UploadFile):
    pass
