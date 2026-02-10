from app.database import SessionLocal, init_db
from app.models.category import Category
from app.models.product import Product

def create_categories(db):

    categories_data = [
        {"name": "Кроссовки", "slug": "sneakers"},     
        {"name": "Ботинки", "slug": "boots"},           
        {"name": "Классическая обувь", "slug": "formal"},         
        {"name": "Спортивная обувь", "slug": "running"},       
    ]

    categories = {}
    for cat_data in categories_data:
        existing = db.query(Category).filter(Category.slug == cat_data["slug"]).first()
        if not existing:
            category = Category(**cat_data)
            db.add(category)
            db.commit()
            db.refresh(category)
            categories[cat_data["slug"]] = category
        else:
            categories[cat_data["slug"]] = existing

    return categories


def create_products(db, categories):

    products_data = [
        {
            "name": "Городские Air Max",
            "description": "Стильные повседневные кроссовки с технологией воздушной амортизации. Идеально подходят для уличного стиля и комфорта в течение всего дня.",
            "price": 129.99,
            "category_id": categories["sneakers"].id,
            "image_url": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500"
        },
        {
            "name": "Белые Ретро Кеды",
            "description": "Классические белые кожаные кроссовки. Минималистичный дизайн, который подходит к любому наряду. Износостойкая резиновая подошва.",
            "price": 89.99,
            "category_id": categories["sneakers"].id,
            "image_url": "https://images.unsplash.com/photo-1552346154-21d32810aba3?w=500" 
        },
        {
            "name": "Высокие кеды",
            "description": "Легендарные текстильные кеды с высокой щиколоткой. Дышащий материал, идеальный выбор для летних прогулок.",
            "price": 59.99,
            "category_id": categories["sneakers"].id,
            "image_url": "https://images.unsplash.com/photo-1607522370275-f14206abe5d3?w=500"
        },

        {
            "name": "Зимние кожаные ботинки",
            "description": "Кожаные ботинки премиум-класса. Водонепроницаемое покрытие и теплая подкладка для холодных зимних дней.",
            "price": 189.99,
            "category_id": categories["boots"].id,
            "image_url": "https://images.unsplash.com/photo-1608256246200-53e635b5b65f?w=500" 
        },
        {
            "name": "Черные Челси",
            "description": "Элегантные ботинки челси из натуральной кожи. Без шнурков, легко надеваются, отлично смотрятся как с джинсами, так и с брюками.",
            "price": 149.99,
            "category_id": categories["boots"].id,
            "image_url": "https://images.unsplash.com/photo-1638247025967-b4e38f787b76?w=500" 
        },

        {
            "name": "Классические Оксфорды",
            "description": "Кожаные туфли Оксфорд ручной работы. Золотой стандарт для деловых костюмов и торжественных мероприятий.",
            "price": 249.99,
            "category_id": categories["formal"].id,
            "image_url": "https://images.unsplash.com/photo-1614252369475-531eba835eb1?w=500"
        },
        {
            "name": "Бархатные Лоферы",
            "description": "Роскошные бархатные лоферы с кисточками. Позвольте себе выделиться на следующей вечеринке.",
            "price": 199.99,
            "category_id": categories["formal"].id,
            "image_url": "https://images.unsplash.com/photo-1533867617858-e7b97e0605df?w=500"
        },

        {
            "name": "Профессиональные беговые",
            "description": "Профессиональная обувь для бега. Ультралегкие материалы и пена с высоким возвратом энергии. Подходят для марафонов.",
            "price": 159.99,
            "category_id": categories["running"].id,
            "image_url": "https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?w=500"
        },
        {
            "name": "Кроссовки для трейла",
            "description": "Прочные кроссовки для бега по пересеченной местности с агрессивным протектором. Защищают стопу на неровных поверхностях.",
            "price": 139.99,
            "category_id": categories["running"].id,
            "image_url": "https://images.unsplash.com/photo-1584735175315-9d5df23860e6?w=500" 
        }
    ]

    count = 0
    for product_data in products_data:
        existing = db.query(Product).filter(Product.name == product_data["name"]).first()
        if not existing:
            product = Product(**product_data)
            db.add(product)
            count += 1
    
    db.commit()
    print(f"✅ Создано товаров: {count}")


def seed_database():
    print("🚀 Запуск заполнения базы данных...")

    init_db()
    
    db = SessionLocal()

    try:
        print("📁 Проверка категорий...")
        categories = create_categories(db)
        
        print("📦 Проверка товаров...")
        create_products(db, categories)

        print("🎉 База данных успешно заполнена!")

    except Exception as e:
        print(f"❌ Ошибка при заполнении: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    seed_database()