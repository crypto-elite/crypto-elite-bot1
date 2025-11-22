import asyncpg
from bot.config import DATABASE_URL

async def connect_db():
    return await asyncpg.connect(DATABASE_URL)

async def create_tables():
    conn = await connect_db()

    await conn.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id BIGINT PRIMARY KEY,
        full_name TEXT,
        username TEXT,
        plan TEXT DEFAULT 'none',
        expires_at TIMESTAMP,
        joined_at TIMESTAMP DEFAULT NOW(),
        last_active TIMESTAMP DEFAULT NOW()
    );
    """)

    await conn.close()

async def add_user(user_id, full_name, username):
    conn = await connect_db()
    await conn.execute("""
        INSERT INTO users (user_id, full_name, username)
        VALUES ($1, $2, $3)
        ON CONFLICT (user_id) DO NOTHING;
    """, user_id, full_name, username)
    await conn.close()

async def update_last_active(user_id):
    conn = await connect_db()
    await conn.execute("""
        UPDATE users SET last_active = NOW()
        WHERE user_id = $1;
    """, user_id)
    await conn.close()

async def get_user(user_id):
    conn = await connect_db()
    row = await conn.fetchrow("SELECT * FROM users WHERE user_id = $1", user_id)
    await conn.close()
    return row
