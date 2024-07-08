from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Definování základního modelu
Base = declarative_base()

# Definice tabulky pro položky v košíku
class CartItem(Base):
    __tablename__ = 'cart_items'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)

# Vytvoření připojení k PostgreSQL databázi
DATABASE_URL = "postgresql+psycopg2://koyeb-adm:XQc0HOTwa1Kl@ep-sweet-thunder-a221r1bm.eu-central-1.pg.koyeb.app/sandbox?sslmode=require"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

# Vytvoření session
Session = sessionmaker(bind=engine)
session = Session()

def add_to_cart(name, quantity, price):
    new_item = CartItem(name=name, quantity=quantity, price=price)
    session.add(new_item)
    session.commit()
    print("Item added to cart")

def delete_from_cart(item_id):
    item = session.query(CartItem).filter_by(id=item_id).first()
    if item:
        session.delete(item)
        session.commit()
        print("Item deleted from cart")
    else:
        print("Item not found")

def edit_cart_item(item_id, name, quantity, price):
    item = session.query(CartItem).filter_by(id=item_id).first()
    if item:
        item.name = name
        item.quantity = quantity
        item.price = price
        session.commit()
        print("Item updated")
    else:
        print("Item not found")

def clear_cart():
    session.query(CartItem).delete()
    session.commit()
    print("Cart cleared")

def search_in_cart(name_query):
    items = session.query(CartItem).filter(CartItem.name.ilike(f'%{name_query}%')).all()
    if items:
        for item in items:
            print(f"ID: {item.id}, Name: {item.name}, Quantity: {item.quantity}, Price: {item.price}")
    else:
        print("No items found")

def view_cart():
    items = session.query(CartItem).all()
    if items:
        for item in items:
            print(f"ID: {item.id}, Name: {item.name}, Quantity: {item.quantity}, Price: {item.price}")
    else:
        print("Cart is empty")

def main():
    while True:
        print("\nOptions:")
        print("1. Add an item to cart")
        print("2. Delete an item from the cart")
        print("3. Edit an item in the cart")
        print("4. Clear the cart")
        print("5. Search in the cart")
        print("6. View the cart contents")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter item name: ")
            quantity = int(input("Enter item quantity: "))
            price = int(input("Enter item price: "))
            add_to_cart(name, quantity, price)
        elif choice == '2':
            item_id = int(input("Enter item ID to delete: "))
            delete_from_cart(item_id)
        elif choice == '3':
            item_id = int(input("Enter item ID to edit: "))
            name = input("Enter new item name: ")
            quantity = int(input("Enter new item quantity: "))
            price = int(input("Enter new item price: "))
            edit_cart_item(item_id, name, quantity, price)
        elif choice == '4':
            clear_cart()
        elif choice == '5':
            name_query = input("Enter item name to search: ")
            search_in_cart(name_query)
        elif choice == '6':
            view_cart()
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again")

if __name__ == "__main__":
    main()
