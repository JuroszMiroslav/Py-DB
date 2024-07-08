import pyodbc

class MSSQLDatabase:
    def __init__(self, server, username, password, database):
        self.server = server
        self.username = username
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        connection_string = (
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={self.server};'
            f'DATABASE={self.database};'
            f'UID={self.username};'
            f'PWD={self.password}'
        )
        self.connection = pyodbc.connect(connection_string)
        self.cursor = self.connection.cursor()
        print("Připojeno k databázi.")

    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Odpojeno od databáze.")

    def execute_query(self, query):
        self.cursor.execute(query)
        self.connection.commit()
        print("Dotaz byl úspěšně proveden.")


# Přihlašovací údaje k databázi
server = 'testmiro.database.windows.net'  # Např. 'localhost' nebo 'your_server.database.windows.net'
username = 'miro'  # Vaše uživatelské jméno
password = 'Ostrava10.'  # Vaše heslo
database = 'testDB'  # Název vaší databáze

# Inicializace připojení k databázi
db = MSSQLDatabase(server, username, password, database)
db.connect()

# Vytvoření uložených procedur
create_procedures_query = '''

'''


db.execute_query(create_procedures_query)

# Odpojení od databáze
db.disconnect()

print("Uložené procedury byly úspěšně vytvořeny v databázi 'testDB'.")