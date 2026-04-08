# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build scalable and production-ready REST APIs using FastAPI, a modern Python web framework. You will understand request handling, data validation, and best practices for API design.

## 📝 Tasks

### 🛠️ Create a Basic FastAPI Application

#### Description
Set up a FastAPI project and create a simple API with GET and POST endpoints. Your API should handle basic HTTP requests and responses.

#### Requirements
Completed program should:

- Initialize a FastAPI application with proper imports
- Create at least one GET endpoint that returns JSON data
- Create at least one POST endpoint that accepts JSON input
- Return appropriate HTTP status codes (200 for success, 201 for creation)
- Use Python type hints for request and response data


### 🛠️ Implement Data Validation and Models

#### Description
Use Pydantic models to validate incoming request data and ensure data consistency. Create robust endpoints that handle invalid input gracefully.

#### Requirements
Completed program should:

- Define at least two Pydantic models for request/response data
- Implement automatic request validation using FastAPI
- Return appropriate error responses (400) when validation fails
- Include optional fields and default values in models
- Add field descriptions and examples in Pydantic models


### 🛠️ Add Path and Query Parameters

#### Description
Extend your API to handle path parameters (e.g., `/items/{item_id}`) and query parameters (e.g., `?skip=0&limit=10`) for more flexible data retrieval.

#### Requirements
Completed program should:

- Create endpoints that accept path parameters
- Implement query parameters with optional and required values
- Add parameter validation (e.g., minimum/maximum values)
- Return filtered or paginated results based on parameters
- Document parameters with descriptions and examples
