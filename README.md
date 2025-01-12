# FastAPI Project: Social Hub

Social Hub is a dynamic web application built with FastAPI for seamless and efficient backend services. It includes features like user authentication, post creation, and more.

## Features

- **User Authentication**: Secure login and signup functionality.
- **CRUD Operations**: Create, read, update, and delete posts.
- **PostgreSQL Integration**: Backend powered by a relational database.
- **RESTful API**: Fully documented API with Swagger UI.
- **Deployed on Render**: Easily accessible through a live deployment.

## Tech Stack

- **Backend**: FastAPI
- **Database**: PostgreSQL
- **Deployment**: Render
- **Other Tools**: SQLAlchemy, Psycopg2

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Devanshi-Sonara/fastapi-practice.git
   cd fastapi-practice
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Set up the environment variables: Create a .env file and add the following:
   ```bash
   DATABASE_URL=your_postgres_connection_url

5. Run the application locally:
   ```bash
   uvicorn main:app --reload

6. Visit the API docs:
    Swagger UI: http://127.0.0.1:8000/docs
    ReDoc: http://127.0.0.1:8000/redoc

## Deployment
The application is deployed on Render. You can access the live version here:

**Deployed API Documentation**: Live API Docs : https://fastapi-devanshi.onrender.com/docs

## Contributing
Contributions are welcome! Please fork the repository and create a pull request.

