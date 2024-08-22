
# AI POWERED CHATBOT APPLICATION

This is a full-stack chatbot application built using React with TypeScript for the frontend and Python with FastAPI for the backend. The application leverages the OpenAI GPT-3.5 Turbo model to generate responses, Redis for caching, and PostgreSQL as the database. Unit tests are implemented using Pytest. All dependencies are installed and managed inside a virtual environment.

## Table of Contents

- Flow Diagram
- Features
- Installation
- Backend Setup
  - Python Virtual Environment
  - Database Setup
  - Environment Variables
  - Redis Setup
  - Running the Backend
  - Testing the Backend
- Frontend Setup
  - Installing Node.js and React
  - Running the Frontend
- Folder Structure
- API Endpoints
- Running Unit Tests

## FLOW DIAGRAM

![Alt text](/flowchart.jpg)

## Features

- **Frontend**: Developed using React with TypeScript, providing a dynamic chat interface.
- **Backend**: Built with FastAPI for handling API requests.
- **Database**: PostgreSQL is used for storing chat messages.
- **Caching**: Redis is used to cache responses to improve performance.
- **Unit Testing**: Pytest is used for creating unit tests to ensure application reliability.

## Installation

### Prerequisites

Before you begin, ensure you have the following installed on your machine:

- Python 3.8+
- Node.js (with npm or yarn)
- PostgreSQL
- Redis

### Respository Setup

``` 
git clone https://github.com/SaiSriramKurapati/chatBot.git
cd chatBot
```

### Backend Setup

1. Create and activate a virtual environment

   ``` 
    python3 -m venv env
    source env/bin/activate
   ```
2. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

#### Database Setup

1. Install PostgreSQL (if not already installed).
2. Create a database:

   ```
   CREATE DATABASE chat_db;
   ```
3. Update the database configuration:

Modify config.yml in the backend directory:
   ```
   database:
    main: "postgresql://<username>:<password>@localhost/chat_db"
    test: "postgresql://<username>:<password>@localhost/test_db"
 ```
Replace <username> and <password> with your PostgreSQL credentials.

#### Environment Variables

1. Setup Environment Variables

   Create a .env file in the backend directory with the following content:
   ```
   DATABASE_URL=postgresql://<username>:<password>@localhost/chat_db
   REDIS_HOST=localhost
   REDIS_PORT=6379
   OPENAI_API_KEY=your-openai-api-key
   ```
   Replace <username>, <password>, and your-openai-api-key with your actual values.

#### Redis Setup

```
brew install redis
```

#### Running the Backend

```
uvicorn app.main:app --reload
```
The backend API should now be running on http://127.0.0.1:8000.

#### Unit Testing 

```
pytest
```

### Frontend Setup

#### Installing Node.js

1. Install Node.js and npm:
    
    ```
    brew install node
    ```
2. Navigate to the frontend directory:

    ```
    cd ../frontend
    ```
3. Install the dependencies

   ```
   npm install
   ```

#### Run Frontend

```
npm start
```
The frontend should now be running on http://localhost:3000.

## Folder Structure

```
chat-widget/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── crud.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── tests/
│   │   └── ...
│   ├── requirements.txt
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── ChatBox.tsx
│   │   │   ├── ChatBubble.tsx
│   │   │   ├── ChatOptions.tsx
│   │   │   ├── FooterForm.tsx
│   │   │   └── ...
│   │   ├── App.tsx
│   │   └── ...
│   ├── package.json
│   └── ...
└── README.md
```
## API ENDPOINTS

- POST /messages/ - Send a message to the bot and receive a response.
- PUT /messages/{id} - Update an existing message.
- DELETE /messages/{id} - Delete a message and all subsequent messages.
- GET /messages/ - Retrieve all messages (for receiving cached response).
