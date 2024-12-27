import sqlite3

def create_db():
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        hobby TEXT
    )
    ''')
    conn.commit()
    conn.close()


def add_client(name, age, hobby):
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO clients (name, age, hobby) VALUES (?, ?, ?)
    ''', (name, age, hobby))
    conn.commit()
    conn.close()

# Функция для получения всех клиентов
def get_all_clients():
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients')
    clients = cursor.fetchall()
    conn.close()
    return clients

def update_client_name(client_id, new_name):
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE clients SET name = ? WHERE id = ?
    ''', (new_name, client_id))
    conn.commit()
    conn.close()


def delete_client(client_id):
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()
    cursor.execute('''
    DELETE FROM clients WHERE id = ?
    ''', (client_id,))
    conn.commit()
    conn.close()

create_db()

add_client("Канеки", 18, "Чтение")
add_client("Хинато", 17, "Спорт")


clients = get_all_clients()
for client in clients:
    print(client)


update_client_name(1, "Сато")


delete_client(2)


clients = get_all_clients()
for client in clients:
    print(client)
