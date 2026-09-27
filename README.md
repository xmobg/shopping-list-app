# Shopping List App

A simple web app for managing personal shopping lists, built with Flask. Users can register, log in, create multiple named lists (e.g. "Седмичен пазар", "Партита"), add items to each list with a quantity and category, and check items off as they're bought.

## Features

- User registration and login (passwords hashed with Werkzeug)
- Session-based authentication
- Create, view, and delete multiple shopping lists per user
- Add, check off ("bought"), and delete items within a list
- Clean, responsive UI styled with vanilla CSS (no frameworks)

## Tech Stack

- **Backend:** Python, Flask
- **Database:** SQLite via Flask-SQLAlchemy
- **Frontend:** HTML, Jinja2 templates, vanilla CSS

## Project Structure

```
shopping_list_app/
├── app.py              # Routes and app entry point
├── models.py           # SQLAlchemy models: User, ShoppingList, Item
├── requirements.txt
├── templates/
│   ├── register.html
│   ├── login.html
│   ├── dashboard.html
│   └── list.html
└── static/
    └── css/
        └── style.css
```

## Setup

1. Clone the repo and navigate into the project folder:
   ```
   git clone https://github.com/xmobg/shopping-list-app.git
   cd shopping-list-app
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # macOS/Linux
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the app:
   ```
   python app.py
   ```

5. Open `http://127.0.0.1:5000` in your browser.

## Data Model

- **User** — id, name, email, username, password (hashed)
- **ShoppingList** — id, name, user_id (FK → User)
- **Item** — id, name, quantity, category, is_bought, list_id (FK → ShoppingList)

Each user can have multiple shopping lists, and each list can contain multiple items.

## Notes

This project was built as a learning exercise to practice Flask, SQLAlchemy relationships, session-based auth, and hand-written CSS.
