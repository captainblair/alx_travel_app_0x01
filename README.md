# ALX Travel App API

This project is a travel booking application built with Django and Django REST Framework.  
It provides a RESTful API for managing travel listings, bookings, and reviews.

## Features
- Listings management (travel destinations, accommodations, etc.)
- Booking system with availability checking
- User authentication and permissions
- API documentation with Swagger/ReDoc
- Pagination and filtering
- Database seeding for development

## Setup

1. Clone the repository
2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```
   python manage.py migrate
   ```
5. Create a superuser (optional, for admin access):
   ```
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```
   python manage.py runserver
   ```

## API Documentation

Once the server is running, you can access the API documentation at:
- Swagger UI: http://127.0.0.1:8000/api/swagger/
- ReDoc: http://127.0.0.1:8000/api/redoc/

## Available Endpoints

### Listings
- `GET /api/listings/` - List all listings
- `POST /api/listings/` - Create a new listing (authenticated)
- `GET /api/listings/{id}/` - Retrieve a specific listing
- `PUT /api/listings/{id}/` - Update a listing (owner only)
- `DELETE /api/listings/{id}/` - Delete a listing (owner only)

### Bookings
- `GET /api/bookings/` - List all bookings (authenticated)
- `POST /api/bookings/` - Create a new booking (authenticated)
- `GET /api/bookings/{id}/` - Retrieve a specific booking (owner only)
- `PUT /api/bookings/{id}/` - Update a booking (owner only)
- `DELETE /api/bookings/{id}/` - Delete a booking (owner only)

## Authentication

The API uses session-based authentication for the web interface and basic authentication for API requests. To authenticate:

1. Session Authentication: Log in via the Django admin or login page
2. Basic Authentication: Include your credentials in the request headers:
   ```
   Authorization: Basic <base64-encoded-username:password>
   ```

## Testing

To run tests:
```
python manage.py test
```

## Seeding the Database

To populate the database with sample data:
```
python manage.py seed_listings --count=10
```

## Requirements

- Python 3.8+
- Django 4.2+
- Django REST Framework 3.14+
- drf-yasg 1.21+

## License

This project is licensed under the MIT License.
