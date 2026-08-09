# Restaurant Table Booking & Food Ordering System

A Django web application for booking restaurant tables and ordering food online.
Built as a portfolio project demonstrating core Django concepts: authentication,
models & relationships, forms, and the Django admin panel.

## Features
- User signup/login (customers)
- Browse menu by category
- Add items to cart and place orders
- Book a table for a chosen date/time (prevents double-booking automatically)
- View booking and order history
- Manage everything (tables, menu, bookings, orders) via Django Admin

## Tech Stack
- Python 3 + Django 5
- SQLite (default, easy to swap for PostgreSQL later)
- Django Templates + plain CSS (Bootstrap can be swapped in later)

## Project Structure
```
restaurant_booking/
├── manage.py
├── restaurant_booking/   # project settings, urls
├── accounts/             # signup / login
├── menu/                 # categories & menu items
├── bookings/             # table booking logic
├── orders/                # cart & order management
├── templates/            # shared base.html, home.html
└── static/css/           # styling
```

## Setup Instructions

1. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate        # Windows: venv\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Apply migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create an admin (superuser) account**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```
   Visit http://127.0.0.1:8000/

6. **Add data via the admin panel**
   Go to http://127.0.0.1:8000/admin/, log in with your superuser account, and add:
   - A few `Table` entries (table number + capacity)
   - `Category` entries (e.g. Starters, Main Course, Desserts)
   - `MenuItem` entries under each category

## Next Steps / Stretch Goals
- Deploy for free on Render or PythonAnywhere
- Add email confirmation for bookings
- Integrate a payment gateway (Razorpay/Stripe test mode)
- Add star ratings/reviews for menu items
- Build a proper admin dashboard with booking analytics
- Push to GitHub with a good README and screenshots — this is what recruiters look at

## Author
Varukuti Venkata Thirupathi Rao
