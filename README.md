# Email Document Listing Application

A secure web application for listing and managing email documents with authentication.

## Features

- Secure user authentication
- Email listing with sender, subject, and timestamp
- Document attachment management
- Search and filtering capabilities
- Modern UI with React
- RESTful API with FastAPI
- MongoDB database integration
- Gmail API integration

## Project Structure

```
email-doc-listing/
├── frontend/           # React frontend application
├── backend/           # FastAPI backend application
└── README.md
```

## Setup Instructions

### Prerequisites

- Node.js (v16 or higher)
- Python (v3.8 or higher)
- MongoDB
- Gmail API credentials

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your credentials
   ```

5. Run the backend server:
   ```bash
   uvicorn main:app --reload
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your API URL
   ```

4. Start the development server:
   ```bash
   npm start
   ```

## API Documentation

Once the backend server is running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Security Features

- JWT-based authentication
- Password hashing with bcrypt
- CORS protection
- Rate limiting
- Input validation
- Secure session management

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request 