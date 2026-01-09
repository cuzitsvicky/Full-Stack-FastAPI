# Vicky Product Tracker - Product Inventory Management System

A full-stack web application for managing product inventory with a FastAPI backend and React frontend.

## Tech Stack

- **Backend**: FastAPI, SQLAlchemy, PostgreSQL
- **Frontend**: React, Axios, CSS3
- **Database**: PostgreSQL

## Project Structure

```
Full Stack Project/
├── main.py                 # FastAPI application & API routes
├── models.py              # Pydantic models
├── database_models.py     # SQLAlchemy database models
├── database.py            # Database configuration
├── frontend/              # React application
│   ├── public/
│   │   ├── index.html
│   │   └── manifest.json
│   ├── src/
│   │   ├── App.js         # Main React component
│   │   ├── App.css        # App styles
│   │   ├── TaglineSection.js  # Tagline section component
│   │   ├── TaglineSection.css # Tagline styles
│   │   ├── index.js       # React entry point
│   │   └── index.css      # Global styles
│   └── package.json       # Frontend dependencies
└── venv/                  # Python virtual environment
```

## Features

✅ **Product Management**
- Create, Read, Update, Delete (CRUD) products
- Real-time product list display
- Search products by ID, name, or description

✅ **Sorting & Filtering**
- Sort by ID, name, price, or quantity
- Toggle between ascending and descending order
- Live search filter

✅ **User Experience**
- Auto-dismissing success/error messages
- Loading indicators
- Confirmation dialog for delete operations
- Responsive design

## Setup Instructions

### Prerequisites
- Python 3.8+
- Node.js & npm
- PostgreSQL

### Backend Setup

1. **Create and activate virtual environment:**
   ```powershell
   python -m venv venv
   & ".\venv\Scripts\Activate.ps1"
   ```

2. **Install Python dependencies:**
   ```powershell
   pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic
   ```

3. **Configure database connection:**
   Edit `database.py` and update the PostgreSQL connection string:
   ```python
   db_url = "postgresql://username:password@localhost:5432/mydatabase"
   ```

4. **Create database:**
   ```sql
   CREATE DATABASE mydatabase;
   ```

### Frontend Setup

1. **Navigate to frontend directory:**
   ```powershell
   cd frontend
   ```

2. **Install Node dependencies:**
   ```powershell
   npm install
   ```

## Running the Application

### Start Backend Server

```powershell
# Activate virtual environment (if not already active)
& ".\venv\Scripts\Activate.ps1"

# Run FastAPI server with auto-reload
uvicorn main:app --reload
```

Backend will be available at: `http://localhost:8000`

### Start Frontend Development Server

```powershell
# In a new terminal, navigate to frontend directory
cd frontend

# Start React development server
npm start
```

Frontend will be available at: `http://localhost:3000`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check - returns greeting |
| GET | `/products` | Fetch all products |
| GET | `/products/{id}` | Fetch product by ID |
| POST | `/products` | Create new product |
| PUT | `/products/{id}` | Update product by ID |
| DELETE | `/products/{id}` | Delete product by ID |

### Request/Response Examples

**Create Product:**
```json
POST /products
{
  "id": 1,
  "name": "Laptop",
  "discription": "A high-performance laptop",
  "price": 999.99,
  "quantity": 10
}
```

**Response:**
```json
{
  "id": 1,
  "name": "Laptop",
  "discription": "A high-performance laptop",
  "price": 999.99,
  "quantity": 10
}
```

## Database Schema

### Products Table

| Column | Type | Constraints |
|--------|------|-------------|
| id | Integer | Primary Key |
| name | String | Not Null |
| discription | Text | Not Null |
| price | Float | Not Null |
| quantity | Integer | Not Null |

## Troubleshooting

### Backend won't start
- Ensure virtual environment is activated
- Check PostgreSQL is running
- Verify database connection string in `database.py`
- Clear `__pycache__` folders: `Remove-Item -Recurse -Force __pycache__`

### Frontend won't start
- Ensure Node.js is installed: `node --version`
- Delete `node_modules` and reinstall: `npm install`
- Clear npm cache: `npm cache clean --force`

### Database connection errors
- Verify PostgreSQL service is running
- Check credentials in `database.py`
- Ensure database exists: `CREATE DATABASE mydatabase;`

## Author

Created as a Full Stack Project with FastAPI, SQLAlchemy, and React.

---

**Note:** This application uses the field name `discription` (with typo) to match the existing database schema. Ensure consistency across all files when making changes.
