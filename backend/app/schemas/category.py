from pydantic import BaseModel, Field



class CategoryBase(BaseModel):
    name: str = Field(..., min_length=5, max_length=100,
                      description="Название категории")
    slug: str = Field(..., min_length=5, max_length=100,
                      description="URL-friendly название категории")
    

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int = Field(..., description="ID категории")

    class Config:
        from_attributes = True

