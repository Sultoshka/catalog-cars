import sqlite3

# Подключаемся к базе данных (если базы данных нет, она будет создана)
conn = sqlite3.connect('byd_dealership.db')
cursor = conn.cursor()

# Создание таблицы cars (Автомобили)
cursor.execute('''
CREATE TABLE IF NOT EXISTS cars (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    model TEXT NOT NULL,
    year INTEGER NOT NULL,
    price REAL NOT NULL,
    color TEXT,
    engine_type TEXT,
    transmission TEXT,
    mileage INTEGER,
    description TEXT,
    image_url TEXT
)
''')

# Создание таблицы customers (Клиенты)
cursor.execute('''
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT,
    address TEXT
)
''')

# Создание таблицы orders (Заказы)
cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    car_id INTEGER,
    order_date TEXT NOT NULL,
    status TEXT NOT NULL,
    total_price REAL NOT NULL,
    FOREIGN KEY(customer_id) REFERENCES customers(id),
    FOREIGN KEY(car_id) REFERENCES cars(id)
)
''')

# Создание таблицы sales (Продажи)
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER,
    sale_date TEXT NOT NULL,
    payment_method TEXT NOT NULL,
    total_amount REAL NOT NULL,
    FOREIGN KEY(order_id) REFERENCES orders(id)
)
''')

# Создание таблицы employees (Сотрудники)
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT,
    position TEXT NOT NULL,
    salary REAL NOT NULL,
    hire_date TEXT NOT NULL
)
''')

# Создание таблицы test_drives (Тест-драйвы)
cursor.execute('''
CREATE TABLE IF NOT EXISTS test_drives (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    car_id INTEGER,
    drive_date TEXT NOT NULL,
    feedback TEXT,
    FOREIGN KEY(customer_id) REFERENCES customers(id),
    FOREIGN KEY(car_id) REFERENCES cars(id)
)
''')

# Создание таблицы inventory (Инвентарь)
cursor.execute('''
CREATE TABLE IF NOT EXISTS inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    car_id INTEGER,
    stock INTEGER NOT NULL,
    location TEXT,
    FOREIGN KEY(car_id) REFERENCES cars(id)
)
''')

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()

print("База данных успешно создана.")