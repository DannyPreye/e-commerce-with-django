# E-Commerce API

A Django-based e-commerce API that provides functionality for managing products, categories, carts, and more.

## Features

- Product catalog management
- Category management
- Shopping cart functionality
- User authentication
- RESTful API endpoints

## Tech Stack

- **Backend**: Django 3.1.12
- **API**: Django REST Framework
- **Database**: SQLite (default)
- **Authentication**: Django's built-in auth system

## Installation

### Prerequisites
- Python 3.13+
- pip package manager

### Setup Steps

1. Clone the repository
   ```bash
   git clone <your-repo-url>
   cd yt_ecommerce
   ```

2. Create and activate a virtual environment
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (Admin)
   ```bash
   python manage.py createsuperuser
   ```

6. Populate the database with sample data (optional)
   ```bash
   python manage.py populate_db
   ```

7. Run the development server
   ```bash
   python manage.py runserver
   ```

8. Access the API at http://127.0.0.1:8000/

## API Endpoints

The API provides the following endpoints:

- `GET /api/products/`: List all products
- `GET /api/products/<id>/`: Retrieve a specific product
- `GET /api/categories/`: List all categories
- `GET /api/categories/<id>/`: Retrieve a specific category
- `GET /api/cart/`: View shopping cart
- `POST /api/cart/add/`: Add product to cart
- `DELETE /api/cart/remove/<id>/`: Remove product from cart

## Project Structure

```
yt_ecommerce/
├── api/                     # Main app with models, views, etc.
│   ├── management/          # Custom management commands
│   │   └── commands/
│   │       └── populate_db.py # Database seeding command
│   ├── migrations/          # Database migrations
│   ├── models.py            # Data models
│   ├── serializers.py       # API serializers
│   ├── urls.py              # API endpoints
│   └── views.py             # API views
├── ecommerceApi/            # Project settings
│   ├── factory.py           # Factories for testing/seeding
│   ├── settings.py          # Project settings
│   └── urls.py              # Project URL configuration
├── media/                   # User-uploaded media files
├── manage.py                # Django management script
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
```

## Development

### Adding New Features

1. Create models in `api/models.py`
2. Create migrations: `python manage.py makemigrations`
3. Apply migrations: `python manage.py migrate`
4. Create serializers in `api/serializers.py`
5. Create views in `api/views.py`
6. Add URL patterns in `api/urls.py`

### Testing

Run tests with:
```bash
python manage.py test
```

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m 'Add feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
