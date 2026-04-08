"""
FastAPI REST API Starter Code
Build a REST API with FastAPI following the assignment requirements.
"""

from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional, List

# Initialize the FastAPI application
app = FastAPI(
    title="Assignment API",
    description="A REST API built with FastAPI",
    version="1.0.0"
)

# TODO: Define Pydantic models for request/response data
# Example structure:
# class Item(BaseModel):
#     id: int
#     name: str = Field(..., description="Item name")
#     description: Optional[str] = None
#     price: float = Field(..., gt=0)


# TODO: Implement GET endpoint to retrieve data
# @app.get("/items")
# async def get_items(skip: int = 0, limit: int = 10):
#     """Retrieve a list of items with pagination"""
#     pass


# TODO: Implement POST endpoint to create data
# @app.post("/items", status_code=201)
# async def create_item(item: Item):
#     """Create a new item"""
#     pass


# TODO: Implement GET endpoint with path parameter
# @app.get("/items/{item_id}")
# async def get_item(item_id: int):
#     """Retrieve a specific item by ID"""
#     pass


# TODO: Run the application
# Command: uvicorn starter_code:app --reload
