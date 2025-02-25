# Python API

This project implements a RESTful API using Python's FastAPI framework. It provides endpoints for basic CRUD (Create, Read, Update, Delete) operations on a sample dataset.

## Features

- **CRUD Operations**: Manage items with create, read, update, and delete functionalities.
- **FastAPI Framework**: Leverages FastAPI for high performance and easy-to-use API development.
- **Automatic Documentation**: Interactive API docs available through Swagger UI.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/singhvibhanshu/Python-API.git
   cd Python-API
   ```

2. **Install Dependencies**:

   Ensure you have Python 3.7 or higher installed. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Start the API Server**:

   Run the following command:

   ```bash
   uvicorn main:app --reload
   ```

   The API will be accessible at `http://127.0.0.1:8000`.

2. **API Endpoints**:

   - `GET /items/`: Retrieve a list of all items.
   - `GET /items/{item_id}`: Retrieve a specific item by its ID.
   - `POST /items/`: Create a new item.
   - `PUT /items/{item_id}`: Update an existing item by its ID.
   - `DELETE /items/{item_id}`: Delete an item by its ID.

3. **Interactive API Documentation**:

   Once the server is running, you can access the interactive API documentation at `http://127.0.0.1:8000/docs`.

## Example Request

Here's how you can create a new item using `curl`:

```bash
curl -X POST "http://127.0.0.1:8000/items/" \
     -H "Content-Type: application/json" \
     -d '{
           "name": "Sample Item",
           "description": "This is a sample item.",
           "price": 9.99,
           "tax": 0.99
         }'
```

**Response**:

```json
{
  "id": 1,
  "name": "Sample Item",
  "description": "This is a sample item.",
  "price": 9.99,
  "tax": 0.99
}
```

## Dependencies

- `fastapi`: For building the API.
- `uvicorn`: For running the ASGI server.

## Notes

- Ensure your Python environment is set up correctly to run FastAPI applications.
- You can customize the sample dataset or extend the API with additional features as needed.

---