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
conn = psycopg2.connect(**db_params)

# Vytvoření kurzoru
cur = conn.cursor()

# Vložení 10 řádků
data = [
    ('Jan', 25),
    ('Petr', 30),
    ('Karel', 22),
    ('Marie', 28),
    ('Eva', 26),
    ('Lukáš', 24),
    ('Anna', 29),
    ('Tomáš', 27),
    ('Ivana', 23),
    ('Jiří', 31)
]

cur.executemany('''
    INSERT INTO lidi (name, age) VALUES (%s, %s)
''', data)
conn.commit()  # Uložení změn


# Uzavření kurzoru a spojení
cur.close()
conn.close()