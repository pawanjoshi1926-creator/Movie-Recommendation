````markdown
# 🎬 Movie Recommendation API

A production-ready Movie Recommendation System built with **FastAPI** and **Scikit-Learn** using **Content-Based Filtering** with **Cosine Similarity**.

---

## 🚀 Features

- Content-Based Movie Recommendation
- Cosine Similarity
- FastAPI REST API
- APIRouter
- Pydantic Models
- Dependency Injection
- Lifespan Events
- Configuration using `.env`
- Logging
- Interactive Swagger Documentation

---

## 📂 Project Structure

```text
movie_recommender/
│
├── .env
├── .gitignore
├── requirements.txt
├── README.md
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── lifespan.py
│   ├── recommender.py
│   ├── schemas.py
│   ├── logging_config.py
│   │
│   ├── dependencies/
│   │   ├── __init__.py
│   │   └── models.py
│   │
│   └── routers/
│       ├── recommendation.py
│       └── health.py
│
├── artifacts/
│   ├── movies.pkl
│   ├── similarity.pkl
│   └── vectorizer.pkl
│
└── movie_api.log
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd movie_recommender
```

### 2. Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the API

```bash
uvicorn app.main:app --reload
```

Server:

```
http://127.0.0.1:8000
```

---

## 📖 API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

## 📌 Endpoints

### Home

```http
GET /
```

Example Response

```json
{
    "message": "Movie Recommendation API"
}
```

---

### Health Check

```http
GET /health
```

Example Response

```json
{
    "status": "healthy"
}
```

---

### Movie Recommendation

```http
GET /api/v1/recommend?movie=Avatar
```

Example Response

```json
{
    "movie": "Avatar",
    "recommendations": [
        {
            "title": "John Carter",
            "similarity_score": 0.914
        },
        {
            "title": "Guardians of the Galaxy",
            "similarity_score": 0.889
        }
    ]
}
```

---

## ⚙️ Environment Variables

Create a `.env` file in the project root.

```env
APP_NAME=Movie Recommendation API
VERSION=1.0.0
DEFAULT_RECOMMENDATIONS=5
```

---

## 🧠 Recommendation Algorithm

1. Merge important movie features.
2. Convert text to vectors using `CountVectorizer`.
3. Compute cosine similarity.
4. Save processed artifacts.
5. Load artifacts during application startup.
6. Return the most similar movies.

---

## 🛠 Technologies Used

- Python
- FastAPI
- Pandas
- NumPy
- Scikit-Learn
- Pydantic
- Pydantic Settings
- Uvicorn

---

## 📝 Logging

Application logs are written to:

```text
movie_api.log
```

Logging includes:

- Application startup
- Application shutdown
- Recommendation requests
- Warnings
- Unexpected exceptions

---

## 📈 Future Improvements

- User Authentication (JWT)
- Movie Search Endpoint
- Pagination
- Recommendation Caching (Redis)
- PostgreSQL Database
- Docker Support
- CI/CD Pipeline
- Model Versioning (MLflow)
- Unit & Integration Tests
- Deployment on Render/AWS/Azure

---

## 👨‍💻 Author

Built as a learning project to demonstrate how to build a production-style Machine Learning API using FastAPI.
````
