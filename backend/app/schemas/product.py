from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from .category import CategoryResponse

class ProductBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=255, description="Название товара")
    description: Optional[str] = Field(None,description="Описание товара")
    price: float = Field(..., gt=0, description="Стоимость товара в рублях(должна быть больше чем 0)")
    category_id: int = Field(..., description="ID категории")
    image_url: Optional[str] = Field(None, description="Ссылка на изображение товара")
    

class ProductCreate(ProductBase):
    pass

class ProductResponse(BaseModel):
    id: int = Field(...,description="ID товара")
    name: str
    description: Optional[str]
    price: float
    category_id: int
    image_url: Optional[str]
    created_at: datetime
    category: CategoryResponse = Field(...,description="Детали категории товаров")
    

    class Config:
        form_attributes = True

class ProductListResponse(BaseModel):
    products: list[ProductResponse]
    total: int = Field(...,description="Общее количество товаров")