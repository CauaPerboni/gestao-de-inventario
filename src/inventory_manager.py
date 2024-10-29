import sqlite3
import os

DB_PATH = os.path.join('database', 'inventory.db')

def create_table():
    conn = sqlite3.connect(DB_PATH)  
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        quantity INTEGER NOT NULL,
        price REAL NOT NULL
    )
    ''')
    
    conn.commit()
    conn.close()
    print("Tabela 'products' criada ou já existe.")  

def add_product(name, description, quantity, price):
    conn = sqlite3.connect(DB_PATH) 
    cursor = conn.cursor()
    
    cursor.execute('INSERT INTO products (name, description, quantity, price) VALUES (?, ?, ?, ?)',
                   (name, description, quantity, price))
    
    conn.commit()
    conn.close()

def get_product(product_id=None):
    conn = sqlite3.connect(DB_PATH) 
    cursor = conn.cursor()
    
    if product_id:
        cursor.execute('SELECT * FROM products WHERE id = ?', (product_id,))
        product = cursor.fetchone()
        conn.close()
        return product
    else:
        cursor.execute('SELECT * FROM products')
        products = cursor.fetchall()
        conn.close()
        return products

def update_product(product_id, name, description, quantity, price):
    conn = sqlite3.connect(DB_PATH) 
    cursor = conn.cursor()
    
    cursor.execute('UPDATE products SET name = ?, description = ?, quantity = ?, price = ? WHERE id = ?',
                   (name, description, quantity, price, product_id))
    
    conn.commit()
    conn.close()

def delete_product(product_id):
    conn = sqlite3.connect(DB_PATH) 
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
    
    conn.commit()
    conn.close()
