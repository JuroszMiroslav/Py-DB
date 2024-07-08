import psycopg2

# Připojení k databázi
db_params = {
    'dbname': 'sandbox',
    'user': 'koyeb-adm',
    'password': 'XQc0HOTwa1Kl',
    'host': 'ep-sweet-thunder-a221r1bm.eu-central-1.pg.koyeb.app',
    'port': 5432,
    'sslmode': 'require'
}
#1. vytvoreni pripojeni
conn = psycopg2.connect(**db_params)
#2. Vytvoření kurzoru
cur = conn.cursor()
#3. SQL prikaz!
cur.execute('SQL prikaz')

#4. Uložení změn
conn.commit()  
#5. Uzavření kurzoru
cur.close()
#6. Uzavreni spojení
conn.close()