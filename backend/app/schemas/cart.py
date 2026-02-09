from pydantic import BaseModel,Field
from typing import Optional

class CartItemBase(BaseModel):
    product_id: int = Field(...,description="ID товара")
    quantity: int = Field(...,gt = 0, description="Количество товаров(больше нуля)")

class CartItemCreate(CartItemBase):
    pass

class CartItemUpdate(BaseModel):
    product_id: int = Field(...,description="ID товара")
    quantity: int = Field(...,gt = 0, description="Количество товаров(больше нуля)")


class CartItem(BaseModel):
    product_id: int
    name: str = Field(...,description="Название товара")
    price: float = Field(...,description="Стоимость товаров")
    quantity: str = Field(...,description="Количество товаров в корзине")
    subtotal: float = Field(...,description="Общая стоимость товаров в корзине")
    image_url: Optional[str] = Field(None,description="Ссылка на изображение товара")

class CartResponse(BaseModel):
    items: list[CartItem] = Field(...,description="Список товаров в корзине(Массив)")
    total: float = Field(...,description="Общая стоимость корзины")
    items_count: int = Field(...,description="Общее количество товаров в корзине")