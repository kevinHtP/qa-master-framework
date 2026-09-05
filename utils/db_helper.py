import sqlite3

def database_master():
    conn = sqlite3.connect("master_toko.db")
    cursor = conn.cursor() 
    cursor.execute(''' CREATE TABLE IF NOT EXISTS produk (nama TEXT, harga REAL)''')
    cursor.execute('''DELETE FROM produk''')
    cursor.execute('''INSERT INTO produk (nama, harga) VALUES ('Sauce Labs Backpack', 29.99)''')
    conn.commit()
    conn.close()

def ambil_harga(nama_pruduk):
    conn = sqlite3.connect("master_toko.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT harga FROM produk WHERE nama = '{nama_pruduk}'")
    harga = cursor.fetchone()[0]
    conn.close
    return harga