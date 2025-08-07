#!/usr/bin/env python3

# Simple database test script
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from dotenv import load_dotenv
load_dotenv()

from sqlalchemy import create_engine, text
from app.core.config import settings

def test_connection():
    """Test database connection"""
    try:
        print(f"Testing connection to: {settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}")
        print(f"Database: {settings.POSTGRES_DB}")
        print(f"User: {settings.POSTGRES_USER}")
        
        # Create engine
        engine = create_engine(settings.DATABASE_URL, echo=False)
        
        # Test connection
        with engine.connect() as conn:
            # Test basic query
            result = conn.execute(text("SELECT version()")).fetchone()
            print(f"✅ Connected successfully!")
            print(f"📊 PostgreSQL version: {result[0]}")
            
            # Test vector extension
            try:
                vector_result = conn.execute(text("SELECT 'vector'::regtype")).fetchone()
                print(f"🔢 Vector extension available: {vector_result[0]}")
            except Exception as e:
                print(f"⚠️  Vector extension test failed: {e}")
            
        print("✅ Database connection test completed successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return False

if __name__ == "__main__":
    success = test_connection()
    exit(0 if success else 1)