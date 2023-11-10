import os
import shutil
from abc import abstractmethod
from os import getcwd
from typing import Tuple, List

from fastapi import UploadFile

from app.core.use_case.base_use_case import BaseUseCase
from app.domain.product.commands.product_command import ProductCreateModel
from app.domain.product.entities.price import PriceEntity, WholesaleEntity
from app.domain.product.entities.product import ProductEntity, DetailEntity, ImageEntity
from app.domain.product.repositories.product_unit_of_work import ProductUnitOfWork
from app.domain.product.results.product_query_model import ProductReadModel


class CreateProductUseCase(BaseUseCase[Tuple[ProductCreateModel], ProductReadModel]):
    unit_of_work: ProductUnitOfWork

    @abstractmethod
    def __call__(self, args: Tuple[ProductCreateModel, List[UploadFile] | None]) -> bool:
        raise NotImplementedError()


class CreateProductUseCaseImpl(CreateProductUseCase):
    def __init__(self, unit_of_work: ProductUnitOfWork):
        self.unit_of_work = unit_of_work

    @staticmethod
    def save_uploaded_file(file: UploadFile, destination: str):
        try:
            with open(destination, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
        finally:
            file.file.close()

    def __call__(self, args: Tuple[ProductCreateModel, List[UploadFile] | None]) -> bool:
        data, files = args
        serialize_data = data.model_dump()

        # TODO: Se debe de hacer un busqueda por codigo para no insertar de nuevo el mismo producto

        images_path = getcwd() + "\\" + "assets" + "\\" + "images" + "\\" + "upload_images" + "\\"
        os.makedirs(images_path, exist_ok=True)

        uploaded_files = []
        images: list[ImageEntity] = []

        if ((files is None) or (len(files) == 0)) and (len(serialize_data['images']) > 0):
            for image in serialize_data['images']:
                ImageEntity(id_=None, image_path=image['image'])
        else:
            for file in files:
                destination = os.path.join(images_path, file.filename)
                self.save_uploaded_file(file, destination)

                uploaded_files.append(file.filename)
                images.append(ImageEntity(id_=None, image_path=images_path + file.filename))

        product = ProductEntity(
            id_=None,
            code=serialize_data['code'],
            price=PriceEntity(
                id_=None,
                wholesale=[
                    WholesaleEntity(id_=None, wholesale=wholesale_data['wholesale'], status=wholesale_data['status'])
                    for wholesale_data in serialize_data['price']['wholesale']
                ],
                retail=serialize_data['price']['retail'],
            ),
            detail=DetailEntity(
                id_=None,
                **serialize_data['detail']
            ),
            images=images
        )

        try:
            self.unit_of_work.repository.create(product)
        except Exception as _e:
            self.unit_of_work.rollback()
            raise

        self.unit_of_work.commit()

        return True
