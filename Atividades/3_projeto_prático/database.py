import sqlite3

def iniciar():
    conexao = sqlite3.connect('usuarios.db')
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            hashed_password TEXT NOT NULL""")
    conexao.commit()
    conexao.close()

def add_usuario():
    try:
        conexao = sqlite3.connect('usuarios.db')
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO usuarios (username, hashed_password) VALUES (?, ?)", (username, hashed_password))
        conexao.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conexao.close()