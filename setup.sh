#!/bin/bash

# Setup script for the development environment

echo "🛠️  Setting up development environment..."

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "📦 Creating Python virtual environment..."
    python3 -m venv .venv
fi

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source .venv/bin/activate

# Install Python dependencies
echo "📚 Installing Python dependencies..."
pip install -r requirements.txt

# Install Node.js dependencies for frontend
echo "📦 Installing Node.js dependencies..."
cd frontend
npm install

# Setup database
echo "🗄️  Setting up database..."
cd ../backend
python setup_vector.py

echo "✅ Setup complete!"
echo ""
echo "To start development servers:"
echo "  ./dev.sh"
echo ""
echo "To manually start backend:"
echo "  cd backend && source ../.venv/bin/activate && python -m uvicorn app.main:app --reload"
echo ""
echo "To manually start frontend:"
echo "  cd frontend && npm run dev"