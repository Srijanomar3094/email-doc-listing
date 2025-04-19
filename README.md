# 📧 Secure Email Document Listing & Customer Aggregation Report

This repository contains the implementation for both **Task 1** and **Task 2** from the Backend Engineer Screening Assessment. The application is built using **FastAPI**, **MongoDB**, **Streamlit**, and **Gmail API**.

---

## 🧩 Task 1: Secure Email Document Listing App

### 🔐 Features
- User authentication system using FastAPI & MongoDB
- Secure login/logout with hashed passwords
- Gmail API OAuth2 integration to fetch user's inbox
- Streamlit frontend to display:
  - Sender
  - Subject
  - Timestamp
  - Document attachment names
- Downloadable attachment list (filename shown, download via Gmail API optional)

### 💻 Tech Stack
- **Frontend**: Streamlit
- **Backend**: FastAPI
- **Database**: MongoDB (local)
- **Email API**: Gmail API (OAuth2)

---

## 📈 Task 2: Customer Data Aggregation Pipeline

### 🧠 Features
- Aggregates customer order data from MongoDB
- Returns:
  - `customerId`, `name`, `email`
  - `totalSpent`, `averageOrderValue`
  - `favoriteCategory` (resolves ties alphabetically)
  - `loyaltyTier`: Bronze/Silver/Gold
  - `lastPurchaseDate`
  - `isActive`: true if ordered in last 6 months
  - `categoryWiseSpend`: spend breakdown per category
- Excludes customers with totalSpent < 500
- Covers 8 sample customers with different order habits

---

## 🚀 Setup & Run Locally

### ✅ Requirements
- Python 3.10+
- MongoDB running locally
- Gmail API credentials

### 📁 Clone Project

```bash
git clone https://github.com/Srijanomar3094/email-doc-listing.git
cd email-doc-listing
```

### 🔧 Setup Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 🔑 Add Gmail API Credentials
- Go to [Google Cloud Console](https://console.cloud.google.com/)
- Create a project → Enable Gmail API → Create OAuth credentials (Desktop)
- Download `credentials.json` and place it in the root directory

---

## 📂 MongoDB Setup

Start MongoDB if not running:

```bash
sudo systemctl start mongod
```

Insert sample customer order data (for Task 2):

```bash
python backend/sample_data.py
```

---

## 🚦 Run the Backend

```bash
uvicorn backend.main:app --reload
```

Visit: [http://localhost:8000/docs](http://localhost:8000/docs)

Test endpoints like `/auth/register`, `/auth/login`, `/mail/emails`, and `/report/customer-report`.

---

## 🎨 Run the Frontend

```bash
cd frontend
streamlit run app.py
```

Visit: [http://localhost:8501](http://localhost:8501)

---

## 🔌 API Endpoints

### 🔐 Auth
| Method | Endpoint          | Description       |
|--------|-------------------|-------------------|
| POST   | /auth/register     | Register new user |
| POST   | /auth/login        | Login user        |

### 📬 Email
| Method | Endpoint        | Description                      |
|--------|------------------|----------------------------------|
| GET    | /mail/emails     | List recent 10 inbox emails with attachments |

### 📊 Customer Report
| Method | Endpoint                | Description                    |
|--------|-------------------------|--------------------------------|
| GET    | /report/customer-report | Get aggregated customer report |

---

## 🧪 Example Test Case for API

### Login:

```json
POST /auth/login

{
  "email": "tes@gmail.com",
  "password": "test123"
}
```

### Report:

```http
GET /report/customer-report
```

Response:

```json
[
  {
    "customerId": "C001",
    "name": "Alice",
    "email": "alice@example.com",
    "totalSpent": 3200,
    "averageOrderValue": 1066.67,
    "favoriteCategory": "Books",
    "loyaltyTier": "Gold",
    "lastPurchaseDate": "2025-04-01T00:00:00",
    "isActive": true,
    "categoryWiseSpend": {
      "Books": 1700,
      "Electronics": 1500
    }
  }
]
```

---

## 🔒 Security Measures

- Passwords hashed using `bcrypt` via `passlib`
- MongoDB used for credential storage (non-plaintext)
- Gmail API uses OAuth2 for secure access, token not stored
- `.env` and `credentials.json` are gitignored
- No sensitive info exposed in APIs

---

## 📁 Folder Structure

```
email-doc-listing/
├── backend/
│   ├── main.py
│   ├── auth.py
│   ├── gmail.py
│   ├── aggregate.py
│   └── sample_data.py
├── frontend/
│   └── app.py
├── credentials.json
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---
