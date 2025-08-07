# Database test script
import asyncio
import asyncpg
from app.core.config import settings

async def test_connection():
    """Test database connection"""
    try:
        print(f"Testing connection to: {settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}")
        print(f"Database: {settings.POSTGRES_DB}")
        print(f"User: {settings.POSTGRES_USER}")
        
        # Test connection
        conn = await asyncpg.connect(
            host=settings.POSTGRES_HOST,
            port=settings.POSTGRES_PORT,
            user=settings.POSTGRES_USER,
            password=settings.POSTGRES_PASSWORD,
            database=settings.POSTGRES_DB
        )
        
        # Test basic query
        result = await conn.fetchval("SELECT version()")
        print(f"✅ Connected successfully!")
        print(f"📊 PostgreSQL version: {result}")
        
        # Test vector extension
        vector_result = await conn.fetchval("SELECT 'vector'::regtype")
        print(f"🔢 Vector extension available: {vector_result}")
        
        await conn.close()
        
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return False
    
    return True

if __name__ == "__main__":
    success = asyncio.run(test_connection())
    exit(0 if success else 1)