import psycopg2

class PostgreSQLDatabase:
    def __init__(self, host, port, username, password, database):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None
        self.sslmode = 'require'

    def connect(self):
        self.connection = psycopg2.connect(
            host=self.host,
            port=self.port,
            user=self.username,
            password=self.password,
            dbname=self.database,
            sslmode = self.sslmode
        )
        self.cursor = self.connection.cursor()
        print("Připojeno k databázi.")

    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Odpojeno od databáze.")
    
    def fetch_all(self, query):
        try:
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            return rows
        except Exception as e:
            print(f"An error occurred: {e}")
            return None    

    def execute_query(self, query):
        self.cursor.execute(query)
        self.connection.commit()
        print("Dotaz byl úspěšně proveden.")

#Volani
# Přihlašovací údaje k databázi
host = 'ep-sweet-thunder-a221r1bm.eu-central-1.pg.koyeb.app'  # Např. 'localhost'
port = '5432'
username = 'koyeb-adm'  # Vaše uživatelské jméno
password = 'XQc0HOTwa1Kl'  # Vaše heslo
database = 'sandbox'  # Název vaší databáze

# Inicializace připojení k databázi
db = PostgreSQLDatabase(host, port, username, password, database)
db.connect()

# Vytvoření tabulek
# create_tables_query = '''create table test(name int);
# '''

# db.execute_query(create_tables_query)

query ='''
SELECT cisloobjednavky, castka
	 ,MAX(castka) OVER (PARTITION BY EXTRACT(YEAR FROM datum)) AS maxCastka
    ,EXTRACT(YEAR FROM datum) AS rok
	,datum
FROM public.objednavky
'''

rows = db.fetch_all(query)

# Zobrazení výsledků
if rows is not None:
    for radek in rows:
        print(radek)


# Odpojení od databáze
db.disconnect()

print("Tabulky byly úspěšně vytvořeny v databázi 'testDB'.")

