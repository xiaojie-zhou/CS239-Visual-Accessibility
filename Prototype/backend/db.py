import sqlite3

DB_FILE = "tokens.db"

# Create database table for tokens
def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tokens (token TEXT PRIMARY KEY, filename TEXT)''')
    conn.commit()
    conn.close()

def save_token(token, filename):
    """Save token to SQLite database"""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO tokens (token, filename) VALUES (?, ?)", (token, filename))
    conn.commit()
    conn.close()

def get_db_connection():
    """Ensure SQLite allows concurrent access."""
    return sqlite3.connect(DB_FILE, timeout=10, check_same_thread=False)

def get_filename_by_token(token):
    """Fetch a single filename by token from the database"""
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT filename FROM tokens WHERE token = ?", (token,))
    row = c.fetchone()
    conn.close()
    return row[0] if row else None  # Return filename or None if token not found

def clear_token(token):
    """Delete a single token from the database"""
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("DELETE FROM tokens WHERE token = ?", (token,))
    conn.commit()
    conn.close()

def clear_tokens():
    """Not used. Delete all tokens from the database. For our convenience."""
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("DELETE FROM tokens")  # Deletes all rows
    conn.commit()
    conn.close()

def load_tokens():
    """Print tokens from SQLite for debugging (without storing them in memory)."""
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM tokens")
    rows = c.fetchall()
    conn.close()
    print("🔄 Tokens loaded from SQLite:", {row[0]: row[1] for row in rows})  # Prints instead of storing

if __name__ == "__main__":
    init_db()  # Initialize database
    load_tokens()  # Load tokens on startup