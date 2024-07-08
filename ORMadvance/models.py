from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.sql import text
from datetime import datetime

Base = declarative_base()

class Klient(Base):
    __tablename__ = 'klient'
    id = Column(Integer, primary_key=True, autoincrement=True)
    jmeno = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    objednavka = relationship('Objednavka', back_populates='klient')

class Objednavka(Base):
    __tablename__ = 'objednavka'
    id = Column(Integer, primary_key=True, autoincrement=True)
    klient_id = Column(Integer, ForeignKey('klient.id'), nullable=False)
    datum_objednavky = Column(DateTime, default=datetime.utcnow)
    celkova_cena = Column(Float, nullable=False)
    klient = relationship('Klient', back_populates='objednavka')

# Nastavení databáze
DATABASE_URL = 'postgresql+psycopg2://koyeb-adm:XQc0HOTwa1Kl@ep-sweet-thunder-a221r1bm.eu-central-1.pg.koyeb.app/sandbox?sslmode=require'

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)

# CRUD operace

def create_klient(session, jmeno, email):
    klient = Klient(jmeno=jmeno, email=email)
    session.add(klient)
    session.commit()
    return klient

def get_klient(session, klient_id):
    return session.query(Klient).filter_by(id=klient_id).first()

def create_objednavka(session, klient_id, celkova_cena):
    objednavka = Objednavka(klient_id=klient_id, celkova_cena=celkova_cena)
    session.add(objednavka)
    session.commit()
    return objednavka

def get_objednavky_pro_klienta(session, klient_id):
    return session.query(Objednavka).filter_by(klient_id=klient_id).all()

# Vlastní SQL dotaz
def get_klienti_s_objednavkami_vyssi_nez(session, castka):
    sql = text('''
        SELECT k.jmeno, k.email, o.celkova_cena
        FROM klient k
        JOIN objednavka o ON k.id = o.klient_id
        WHERE o.celkova_cena > :castka
    ''')
    return session.execute(sql, {'castka': castka}).fetchall()
