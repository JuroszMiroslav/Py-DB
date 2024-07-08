from models import init_db, Session, create_klient, get_klient, create_objednavka, get_objednavky_pro_klienta, get_klienti_s_objednavkami_vyssi_nez

def main():
    # Inicializace databáze
    init_db()

    # Vytvoření session
    session = Session()

    # Vytvoření klienta
    klient = create_klient(session, 'Petsr Naosvaak', 'jana.naaaovak@example.com')
    print(f'Vytvořen klient: {klient.jmeno}, {klient.email}')

    # Získání klienta
    klient = get_klient(session, klient.id)
    print(f'Získaný klient: {klient.jmeno}, {klient.email}')

    # Vytvoření objednávky pro klienta
    objednavka = create_objednavka(session, klient.id, 1500.0)
    print(f'Vytvořena objednávka: {objednavka.id}, {objednavka.celkova_cena}')

    # Získání objednávek pro klienta
    objednavky = get_objednavky_pro_klienta(session, klient.id)
    for objednavka in objednavky:
        print(f'Objednávka ID: {objednavka.id}, Cena: {objednavka.celkova_cena}')

    # Vlastní SQL dotaz
    klienti = get_klienti_s_objednavkami_vyssi_nez(session, 1000)
    for klient in klienti:
        print(f'Klient: {klient.jmeno}, Email: {klient.email}, Cena objednávky: {klient.celkova_cena}')

    # Uzavření session
    session.close()

if __name__ == '__main__':
    main()
