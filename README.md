# Bookstore Project

這是一個使用 Django 框架開發的書店管理系統。該系統提供基本的書籍管理功能，包括書籍的增刪查改。

## 功能特點

- 書籍資訊管理（標題、出版社、出版日期、價格、頁數）
- Django 管理後台介面
- RESTful API 設計

## 技術棧

- Python 3.x
- Django 5.2
- SQLite 資料庫

## 安裝說明

1. 克隆專案到本地：
```bash
git clone [your-repository-url]
cd bookstore
```

2. 創建並啟動虛擬環境：
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# 或
.venv\Scripts\activate  # Windows
```

3. 安裝依賴套件：
```bash
pip install -r requirements.txt
```

4. 執行資料庫遷移：
```bash
python manage.py migrate
```

5. 創建超級用戶（可選）：
```bash
python manage.py createsuperuser
```

6. 啟動開發伺服器：
```bash
python manage.py runserver
```

## 使用說明

1. 訪問管理後台：
   - 網址：http://localhost:8000/admin/
   - 使用超級用戶帳號登入

2. API 端點：
   - 書籍列表：/books/
   - 書籍詳情：/books/<id>/

## 專案結構

```
bookstore/
├── books/                # 主要應用程式
│   ├── models.py        # 資料模型
│   ├── views.py         # 視圖邏輯
│   ├── urls.py          # URL 路由
│   └── templates/       # 模板文件
├── pages/               # 頁面應用程式
├── bookstore/           # 專案配置
├── manage.py            # Django 管理腳本
└── requirements.txt     # 依賴套件列表
```