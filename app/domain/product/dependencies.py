from fastapi import Depends
from sqlalchemy.orm import Session

# Session DB
from app.core.database.database import get_session
# Repositories
from app.domain.product.repositories.product_repository import ProductRepository
# Unit of work
from app.domain.product.repositories.product_unit_of_work import ProductUnitOfWork
# Services and Services Impl
from app.domain.product.services.product_query_service import ProductQueryService
# Use cases and  Use cases Impl
from app.domain.product.use_cases.create_product import CreateProductUseCase, CreateProductUseCaseImpl
from app.domain.product.use_cases.delete_product import DeleteProductUseCase, DeleteProductUseCaseImpl
from app.domain.product.use_cases.get_product import GetProductUseCase, GetProductUseCaseImpl
from app.domain.product.use_cases.get_products import GetProductsUseCase, GetProductsUseCaseImpl
from app.domain.product.use_cases.massively_create import MassivelyCreateUseCase, MassivelyCreateUseCaseImpl
from app.domain.product.use_cases.update_product import UpdateProductUseCase, UpdateProductUseCaseImpl
# Repositories Impl
from app.infrastructure.product.repositories.product_repository_impl import ProductRepositoryImpl
# Unit of work Impl
from app.infrastructure.product.repositories.product_unit_of_work_ompl import ProductUnitOfWorkImpl
from app.infrastructure.product.services.product_query_service_impl import ProductQueryServiceImpl


def get_product_query_service(session: Session = Depends(get_session)) -> ProductQueryService:
    return ProductQueryServiceImpl(session)


# Repository
def get_product_repository(session: Session = Depends(get_session)) -> ProductRepository:
    return ProductRepositoryImpl(session=session)


def get_product_unit_of_work(
        product_repository: ProductRepository = Depends(get_product_repository),
        session: Session = Depends(get_session)
) -> ProductUnitOfWork:
    return ProductUnitOfWorkImpl(session=session, product_repository=product_repository)


def get_massively_create_use_case(
        unit_of_work: ProductUnitOfWork = Depends(get_product_unit_of_work)
) -> MassivelyCreateUseCase:
    return MassivelyCreateUseCaseImpl()


def get_create_product_use_case(
        unit_of_work: ProductUnitOfWork = Depends(get_product_unit_of_work)
) -> CreateProductUseCase:
    return CreateProductUseCaseImpl(unit_of_work=unit_of_work)


def get_products_use_case(
        products_query_service: ProductQueryService = Depends(get_product_query_service)
) -> GetProductsUseCase:
    return GetProductsUseCaseImpl(products_query_service)


def get_product_use_case(
        product_query_service: ProductQueryService = Depends(get_product_query_service)
) -> GetProductUseCase:
    return GetProductUseCaseImpl(product_query_service)


def get_delete_product_use_case(
        unit_of_work: ProductUnitOfWork = Depends(get_product_unit_of_work)
) -> DeleteProductUseCase:
    return DeleteProductUseCaseImpl(unit_of_work=unit_of_work)


def get_update_product_use_case(
        unit_of_work: ProductUnitOfWork = Depends(get_product_unit_of_work)
) -> UpdateProductUseCase:
    return UpdateProductUseCaseImpl(unit_of_work)
