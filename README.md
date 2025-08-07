# Next.js + FastAPI + PostgreSQL Vector Database Development Environment

A complete full-stack development environment with Next.js frontend, FastAPI backend, and PostgreSQL with vector support.

## 🚀 Quick Start

### 1. Setup Environment
```bash
./setup.sh
```

### 2. Start Development Servers
```bash
./dev.sh
```

### 3. Access Applications
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## 📁 Project Structure

```
├── frontend/                 # Next.js 14 frontend
│   ├── src/
│   │   ├── app/           # App Router
│   │   ├── components/    # React components
│   │   └── lib/           # Utilities
│   ├── package.json
│   ├── next.config.js
│   └── tailwind.config.js
├── backend/                 # FastAPI backend
│   ├── app/
│   │   ├── main.py        # FastAPI app entry point
│   │   ├── core/          # Core configuration
│   │   ├── models/        # Database models
│   │   ├── schemas/       # Pydantic schemas
│   │   └── api/           # API routes
│   ├── alembic/           # Database migrations
│   └── test_db_simple.py  # Database test script
├── .env                   # Environment variables
├── requirements.txt       # Python dependencies
├── setup.sh              # Setup script
└── dev.sh                # Development server script
```

## 🔧 Configuration

### Environment Variables
```bash
# Database Configuration
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=your_database_name
POSTGRES_USER=your_database_user
POSTGRES_PASSWORD=your_secure_password

# FastAPI Configuration
SECRET_KEY=your-secret-key-here-change-in-production
ACCESS_TOKEN_EXPIRE_MINUTES=10080

# CORS Configuration
BACKEND_CORS_ORIGINS=["http://localhost:3000", "http://localhost:3001", "http://localhost:8080"]
```

## 🗄️ Database Features

### PostgreSQL with Vector Support
- **Database**: PostgreSQL 15.13
- **Vector Extension**: pgvector for vector operations
- **ORM**: SQLAlchemy 2.0 with async support
- **Migrations**: Alembic for database schema management

### Database Models
- **Users**: User management with authentication
- **Documents**: Document storage with vector embeddings

## 🎨 Frontend Features

### Next.js 14 with TypeScript
- **Framework**: Next.js 14 with App Router
- **Styling**: Tailwind CSS
- **Language**: TypeScript
- **State Management**: React hooks
- **API Integration**: Built-in API routes with proxy to backend

## 🔧 Backend Features

### FastAPI with Modern Python
- **Framework**: FastAPI 0.104.1
- **Documentation**: Automatic OpenAPI/Swagger docs
- **Validation**: Pydantic 2.0 for data validation
- **Async Support**: Full async/await support
- **CORS**: Configured for frontend development

### API Endpoints
- `GET /` - Root endpoint
- `GET /health` - Health check
- `GET /api/v1/documents` - List documents
- `POST /api/v1/documents` - Create document
- `GET /api/v1/documents/{id}` - Get document
- `PUT /api/v1/documents/{id}` - Update document
- `DELETE /api/v1/documents/{id}` - Delete document

## 🛠️ Development Commands

### Frontend (Next.js)
```bash
cd frontend
npm install          # Install dependencies
npm run dev         # Start development server
npm run build       # Build for production
npm run start       # Start production server
npm run lint        # Run linting
```

### Backend (FastAPI)
```bash
cd backend
source ../.venv/bin/activate  # Activate virtual environment

# Development server
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Database operations
python test_db_simple.py  # Test database connection
python setup_vector.py    # Setup vector extension
alembic upgrade head      # Run migrations
alembic revision --autogenerate -m "description"  # Create migration
```

## 🔍 Testing

### Database Connection
```bash
cd backend
source ../.venv/bin/activate
python test_db_simple.py
```

### API Testing
- Visit http://localhost:8000/docs for interactive API documentation
- Use the built-in Swagger UI to test all endpoints

## 📊 Vector Database Usage

### Storing Vector Embeddings
```python
from app.models.models import Document
from sqlalchemy.orm import Session

# Create document with embedding
document = Document(
    title="Sample Document",
    content="This is a sample document content",
    embedding=[0.1, 0.2, 0.3, ...],  # 1536-dimensional vector
    metadata={"source": "user", "type": "text"}
)

db.add(document)
db.commit()
```

### Vector Similarity Search
```python
from pgvector.sqlalchemy import CosineDistance
from app.models.models import Document

# Find similar documents
query_vector = [0.1, 0.2, 0.3, ...]  # Your query vector
similar_docs = db.query(Document).order_by(
    CosineDistance(Document.embedding, query_vector)
).limit(10).all()
```

## 🚀 Production Deployment

### Environment Setup
1. Update `.env` file with production values
2. Change `SECRET_KEY` to a secure value
3. Update CORS origins for production domains
4. Set up proper database security

### Frontend Deployment
```bash
cd frontend
npm run build
npm run start
```

### Backend Deployment
```bash
cd backend
source ../.venv/bin/activate
pip install gunicorn
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker
```

## 🤝 Contributing

1. Follow the existing code style
2. Add tests for new features
3. Update documentation
4. Use proper error handling
5. Follow security best practices

## 📝 License

This project is licensed under the MIT License.