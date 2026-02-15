# FASTAPI:
FastAPI is a modern and high-performance Python web framework used to build APIs quickly and efficiently. Designed with simplicity it allows developers to create RESTful APIs using Python's type hints which also enable automatic validation and error handling.

# Featurse of FastAPI:

```bash

High Performance -> Fast and async-ready framework built on ASGI.

Automatic Data Validation (via Pydantic)  -> Validates request data using Python type hints.

Automatic API Docs (via Swagger UI) -> Interactive docs available automatically at /docs.

Async / Await Support -> Handles multiple requests efficiently.

Dependency Injection System -> Clean and reusable components with Depends.

Automatic OpenAPI Schema -> Automatically creates OpenAPI JSON schema.

```

# Installation and Setup of FastAPI

```bash

1.  Install Python 3: Make sure Python 3.7 or above is installed.

2. Install FastAPI: Use pip to install the FastAPI library

>>> pip install fastapi[standard]

3. Install Uvicorn (ASGI server): Uvicorn is a lightweight server used to run FastAPI apps

>>> pip install uvicorn

```

## Create a Simple API
```bash
main.py

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
```
#### To run your application, use the fastapi command that the FastAPI CLI provides:
```bash
>>> fastapi dev main.py

# Production mode disables auto-reload and runs with optimized settings suitable for serving real traffic. You use production mode when running your application on a server.
```
You can add the --host or --port flags to define the host and port on which you want to serve the FastAPI app. By default, your application starts on http://127.0.0.1:8000. When you visit this URL in your browser, you’ll see the JSON response:

```bash
 {"message": "Hello, FastAPI!"}
```
## Example:

```bash
from fastapi import FastAPI

app = FastAPI()


@app.post("/greet")
def greet_user(name: str):
    return {"message": "Hello, " + name + "!"}
```
This code creates a POST endpoint /greet that takes a string name and returns a greeting message like "Hello, name!" as JSON.

Similarly, we can perform different CRUD operations like PUT, PATCH and DELETE using FastAPI.

# Advantage of FastAPI
```bash
1. Easy to Learn -> Beginner-friendly syntax with automatic docs makes it quick to get started.

2. High Performance -> Built on async features, it handles many requests efficiently.

3. Auto Data Validation -> Uses type hints to validate input/output automatically.

4. Built-in Auth -> Supports JWT, OAuth2 and custom authentication easily.

5. Middleware Support -> Add logging, auth and more through simple middleware integration.
```

# Disadvantage of FastAPI
```bash
1. Async Complexity -> Requires understanding async/await, which can be tricky for beginners.

2. Fewer Built-in Tools -> Lacks features like Django’s admin panel, ORM or user auth.

3. Smaller Ecosystem -> Fewer plugins, tutorials and community support compared to older frameworks.

4. Debugging Difficulty -> Async debugging is harder than with traditional synchronous code.
```

# Power Your Backend With FastAPI
Real-world APIs need to handle more than friendly greetings. You’ll often need endpoints that accept data, process it, and return meaningful results—for example, when you create a JavaScript Frontend for an API.

FastAPI makes it straightforward to create these common API patterns using path parameters, query parameters, and request bodies.

To try this out, replace the code in main.py with an example that demonstrates three typical API endpoints you might build for a book catalog system:

```bash
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

books = [
    {"id": 1, "title": "Python Basics", "author": "Real P.", "pages": 635},
    {"id": 2, "title": "Breaking the Rules", "author": "Stephen G.", "pages": 99},
]

class Book(BaseModel):
    title: str
    author: str
    pages: int

@app.get("/books")
def get_books(limit: int | None = None):
    """Get all books, optionally limited by count."""
    if limit:
        return {"books": books[:limit]}
    return {"books": books}

@app.get("/books/{book_id}")
def get_book(book_id: int):
    """Get a specific book by ID."""
    for book in books:
        if book["id"] == book_id:
            return book
    return {"error": "Book not found"}

@app.post("/books")
def create_book(book: Book):
    """Create a new book entry."""
    new_book = {
        "id": len(books) + 1,
        "title": book.title,
        "author": book.author,
        "pages": book.pages
    }
    books.append(new_book)
    return new_book
````
This code creates a simple book API using FastAPI. It stores books in a list (like a small temporary database). It allows you to see all books, get one book by its ID, and add a new book. The Book class uses Pydantic to make sure the data you send (title, author, pages) is correct before adding it. In short, this program lets you create and read book data through API endpoints in a simple and structured way.