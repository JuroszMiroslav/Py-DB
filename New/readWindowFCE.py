import psycopg2
from PostgreConnection import PostgreSQLDatabase

host = 'ep-sweet-thunder-a221r1bm.eu-central-1.pg.koyeb.app'  # Např. 'localhost'
port = '5432'
username = 'koyeb-adm'  # Vaše uživatelské jméno
password = 'XQc0HOTwa1Kl'  # Vaše heslo
database = 'sandbox'  # Název vaší databáze

db = PostgreSQLDatabase(host, port, username, password, database)
# Připojení k databázi
conn = db.connect()

# Načtení celé tabulky
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
# Uzavření kurzoru a spojení
db.disconnect()