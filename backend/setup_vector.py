#!/usr/bin/env python3

import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from app.core.config import settings

async def setup_vector_extension():
    """Create pgvector extension if it doesn't exist"""
    
    # Use async database URL for this operation
    async_engine = create_async_engine(
        settings.DATABASE_URL.replace('postgresql://', 'postgresql+asyncpg://'),
        echo=False
    )
    
    async_session = sessionmaker(
        async_engine, class_=AsyncSession, expire_on_commit=False
    )
    
    async with async_session() as session:
        try:
            # Check if pgvector extension exists
            result = await session.execute(
                text("SELECT * FROM pg_extension WHERE extname = 'vector'")
            )
            
            if result.fetchone() is None:
                print("Installing pgvector extension...")
                await session.execute(text("CREATE EXTENSION vector"))
                await session.commit()
                print("pgvector extension installed successfully!")
            else:
                print("pgvector extension already exists")
                
        except Exception as e:
            print(f"Error setting up vector extension: {e}")
            raise
        finally:
            await async_engine.dispose()

if __name__ == "__main__":
    asyncio.run(setup_vector_extension())