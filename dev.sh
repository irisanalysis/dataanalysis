#!/bin/bash

# Development script for the full-stack application

echo "🚀 Starting development environment..."

# Function to cleanup on exit
cleanup() {
    echo "🛑 Stopping development servers..."
    if [ ! -z "$BACKEND_PID" ]; then
        kill $BACKEND_PID 2>/dev/null
    fi
    if [ ! -z "$FRONTEND_PID" ]; then
        kill $FRONTEND_PID 2>/dev/null
    fi
    exit 0
}

# Set up signal handlers
trap cleanup SIGINT SIGTERM

# Start backend server
echo "🔧 Starting FastAPI backend..."
cd backend
source ../.venv/bin/activate 2>/dev/null || echo "⚠️  Virtual environment not found, using system Python"
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8003 &
BACKEND_PID=$!

# Wait a moment for backend to start
sleep 3

# Start frontend server
echo "🎨 Starting Next.js frontend..."
cd ../frontend
npm install
PORT=9003 npm run dev &
FRONTEND_PID=$!

echo "✅ Development environment started!"
echo "📱 Frontend: http://localhost:9003"
echo "🔧 Backend API: http://localhost:8003"
echo "📖 API Docs: http://localhost:8003/docs"
echo ""
echo "Press Ctrl+C to stop all servers"

# Wait for both processes
wait