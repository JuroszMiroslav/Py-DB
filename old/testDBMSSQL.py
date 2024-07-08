import pyodbc

# Přihlašovací údaje k databázi
server = 'testmiro.database.windows.net'  # Např. 'localhost' nebo 'your_server.database.windows.net'
username = 'miro'  # Vaše uživatelské jméno
password = 'Ostrava10.'  # Vaše heslo

# Připojení k MS SQL Serveru
connection_string = (
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={server};'
    f'UID={username};'
    f'PWD={password}'
)
conn = pyodbc.connect(connection_string)
conn.autocommit = True
cursor = conn.cursor()

# Vytvoření databáze "Sports Store"
cursor.execute("IF DB_ID('SportsStore') IS NOT NULL DROP DATABASE SportsStore")
cursor.execute("CREATE DATABASE SportsStore")

# Uzavření počátečního připojení
cursor.close()
conn.close()

# Připojení k nově vytvořené databázi "Sports Store"
connection_string = (
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={server};'
    f'DATABASE=SportsStore;'
    f'UID={username};'
    f'PWD={password}'
)
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

# Vytvoření tabulek
create_tables_query = '''
CREATE TABLE goods (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(100) NOT NULL,
    type NVARCHAR(50) NOT NULL,
    quantity INT NOT NULL,
    cost_price DECIMAL(10, 2) NOT NULL,
    manufacturer NVARCHAR(100) NOT NULL,
    sale_price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE employees (
    id INT IDENTITY(1,1) PRIMARY KEY,
    full_name NVARCHAR(100) NOT NULL,
    position NVARCHAR(50) NOT NULL,
    date_of_employment DATE NOT NULL,
    gender NVARCHAR(10) NOT NULL,
    salary DECIMAL(10, 2) NOT NULL
);

CREATE TABLE clients (
    id INT IDENTITY(1,1) PRIMARY KEY,
    full_name NVARCHAR(100) NOT NULL,
    email NVARCHAR(100) NOT NULL,
    contact_phone NVARCHAR(20),
    gender NVARCHAR(10),
    order_history TEXT,
    discount_percentage DECIMAL(5, 2),
    registration_date DATE NOT NULL,
    subscribed_to_mailing BIT NOT NULL
);

CREATE TABLE sales (
    id INT IDENTITY(1,1) PRIMARY KEY,
    goods_id INT,
    sale_price DECIMAL(10, 2) NOT NULL,
    quantity INT NOT NULL,
    sale_date DATE NOT NULL,
    employee_id INT,
    client_id INT,
    FOREIGN KEY (goods_id) REFERENCES goods(id),
    FOREIGN KEY (employee_id) REFERENCES employees(id),
    FOREIGN KEY (client_id) REFERENCES clients(id)
);
'''

cursor.execute(create_tables_query)

# Potvrzení změn a uzavření připojení
conn.commit()
cursor.close()
conn.close()

print("Databáze a tabulky byly úspěšně vytvořeny v MS SQL Serveru.")
