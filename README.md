# 👟 Shoe Shop — FastAPI + Vue.js 3

Полнофункциональный учебный проект интернет-магазина обуви. 
Бэкенд реализован на **FastAPI**, фронтенд - частично реализован с помощью нейросети на Vue.js 3.

---

## 🛠 Технологический стек

* **Backend:** Python 3.10+, FastAPI, SQLAlchemy, Pydantic, SQLite.
* **Frontend:** Vue 3, Pinia (хранилище), Vue Router, Tailwind CSS, Axios.
* **Database:** SQLite (локальный файл `shop.db`).

---

## Демонстрация

* **Доступна по ссылке:** https://drive.google.com/drive/folders/1WrCBtaNY023bFThhZ4MmCUmlIXuktaxu?usp=sharing

## 🚀 Быстрый запуск (Backend)

1.  **Перейдите в папку бэкенда:**
    ```bash
    cd backend
    ```

2.  **Создайте и активируйте виртуальное окружение:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Установите зависимости:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Запустите сервер:**
    ```bash
    uvicorn app.main:app --reload
    ```
    *API будет доступно по адресу: http://localhost:8000*
    *Интерактивная документация (Swagger): http://localhost:8000/api/docs*

---

## 💻 Запуск фронтенда (Frontend)

1.  **Перейдите в папку фронтенда:**
    ```bash
    cd frontend
    ```

2.  **Установите зависимости:**
    ```bash
    npm install
    ```

3.  **Запустите проект в режиме разработки:**
    ```bash
    npm run dev
    ```
    *Сайт будет доступен по адресу: http://localhost:5173*

---

## 📁 Структура проекта

* `backend/app/models/` — модели базы данных (SQLAlchemy).
* `backend/app/routes/` — эндпоинты API.
* `backend/static/` — статические файлы и изображения товаров.
* `frontend/src/stores/` — управление состоянием (корзина, товары) через Pinia.
* `frontend/src/views/` — страницы приложения.

