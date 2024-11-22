# Pageloot


<div style="color: red; font-weight: bold;">
    Make sure that you have Docker, Docker Compose installed on your local machine.
</div>

## Setup

- **To build project run**: `make`

- **To run migrations**: `make migrate`

- **To run the project**: `make run`

- **To run the tests**: `make test`

- **To run the containers**: `make stop`
    

## API Documentation

[Pageloot](http://localhost:8000/swagger/)

## API Endpoints

### 1. Create User

- **Endpoint**: `POST /users/`
- **Description**: Add a new user

### 2. Create Expense

- **Endpoint**: `POST /expenses/`
- **Description**: Add a new expense.

### 3. Expense Category Summary

- **Endpoint**: `GET /expenses/category-summary/`
- **Description**: Get the summary of expenses.

### 4. Get Filtered Expenses

- **Endpoint**: `GET /expenses/`
- **Description**: Get a list of filteredexpenses.
