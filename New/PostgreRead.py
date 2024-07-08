from models import Uzivatel, get_engine, get_session

# Parametry připojení k databázi
db_params = {
    'dbname': 'sandbox',
    'user': 'koyeb-adm',
    'password': 'XQcOH0Twa1K1',
    'host': 'ep-sweet-thunder-a221rlbm.eu-central-1.pg.koyeb.app',
    'port': 5432,
    'sslmode': 'require'
}

# Vytvoření databázového připojení a session
engine = get_engine(db_params)
session = get_session(engine)

# Vytvoření tabulek
Uzivatel.metadata.create_all(engine)

# CREATE: Přidání nového uživatele
def pridat_uzivatele(jmeno, email, vek):
    novy_uzivatel = Uzivatel(jmeno=jmeno, email=email, vek=vek)
    session.add(novy_uzivatel)
    session.commit()
    print(f"Uživatel {jmeno} přidán do databáze.")

# READ: Načtení všech uživatelů
def nacti_uzivatele():
    uzivatele = session.query(Uzivatel).all()
    for uzivatel in uzivatele:
        print(f"ID: {uzivatel.id}, Jméno: {uzivatel.jmeno}, Email: {uzivatel.email}, Věk: {uzivatel.vek}")

# UPDATE: Aktualizace uživatele
def aktualizuj_uzivatele(id, nove_jmeno=None, novy_email=None, novy_vek=None):
    uzivatel = session.query(Uzivatel).filter_by(id=id).first()
    if uzivatel:
        if nove_jmeno:
            uzivatel.jmeno = nove_jmeno
        if novy_email:
            uzivatel.email = novy_email
        if novy_vek:
            uzivatel.vek = novy_vek
        session.commit()
        print(f"Uživatel s ID {id} byl aktualizován.")
    else:
        print(f"Uživatel s ID {id} nebyl nalezen.")

# DELETE: Smazání uživatele
def smazat_uzivatele(id):
    uzivatel = session.query(Uzivatel).filter_by(id=id).first()
    if uzivatel:
        session.delete(uzivatel)
        session.commit()
        print(f"Uživatel s ID {id} byl smazán.")
    else:
        print(f"Uživatel s ID {id} nebyl nalezen.")

# Příklad použití CRUD operací
if __name__ == '__main__':
    # Přidání uživatele
    pridat_uzivatele("Jan Novák", "jan.novak@example.com", 30)
    
    # Načtení všech uživatelů
    nacti_uzivatele()
    
    # Aktualizace uživatele
    aktualizuj_uzivatele(1, nove_jmeno="Jan Nový", novy_email="jan.novy@example.com")
    
    # Načtení všech uživatelů po aktualizaci
    nacti_uzivatele()
    
    # Smazání uživatele
    smazat_uzivatele(1)
    
    # Načtení všech uživatelů po smazání
    nacti_uzivatele()

# Uzavření session
session.close()
