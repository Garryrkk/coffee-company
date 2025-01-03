
🚧 **This project is currently under active development.**

- The **backend** is being developed to handle user authentication, database management, and API endpoints.
- The **frontend** is under development in a separate repository and will integrate with this backend.

## Features

- User Authentication:
  - Signup
  - Login
  - Password Reset
  - Email Verification
- User Profile Management
- Database Integration using SQLAlchemy
- RESTful API Design

## Technologies Used

- **Python**
- **Flask**
- **SQLAlchemy**
- **Flask-CORS**
- **Flask-Dotenv**

## Installation

### Prerequisites

- Python 3.8+
- Virtual environment tool (e.g., `venv` or `virtualenv`)
- SQLite (default database)

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/coffee-shop-backend.git
   cd coffee-shop-backend
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:

   Create a `.env` file in the root directory and add the following variables:

   ```env
   SECRET_KEY=your-secret-key
   DATABASE_URL=sqlite:///coffee_shop.db
   ```

5. Run the application:

   ```bash
   python app.py
   ```

6. The API will be available at `http://127.0.0.1:5000`.

## Usage

### Available Endpoints

| Endpoint            | Method | Description                      |
|---------------------|--------|----------------------------------|
| `/api/auth/signup`  | POST   | Create a new user account        |
| `/api/auth/login`   | POST   | Log in an existing user          |
| `/api/auth/reset`   | POST   | Reset user password              |

Use a tool like Postman or cURL to test the API endpoints.

## Project Structure

```plaintext
backend/
├── config/
│   ├── __init__.py
│   └── database.py
├── models/
│   ├── __init__.py
│   └── user_model.py
├── routes/
│   ├── __init__.py
│   └── signup.py
├── utils/
│   └── __init__.py
└── __init__.py
app.py
requirements.txt
```

## Contributing

Contributions are welcome! If you would like to help with development, please fork the repository and create a pull request with your changes.

---

🌟 **Star this repository if you find it helpful!**
