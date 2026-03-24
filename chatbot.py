import pandas as pd

df = pd.read_csv("data/cleaned_books.csv")

def search_book(name):
    result = df[df["Title"].str.lower().str.contains(name.lower())]
    
    if result.empty:
        print("❌ No books found")
    else:
        print("\n📚 Results:")
        print(result[["Title", "Price", "Rating", "Availability"]])


def filter_price(max_price):
    result = df[df["Price"] <= max_price]
    print(result[["Title", "Price"]])


def filter_availability():
    result = df[df["Availability"] > 0]
    print(result[["Title", "Availability"]])


def chatbot():
    print("📚 Welcome to BookBot")
    print("Commands:")
    print("1. search book")
    print("2. filter price")
    print("3. available books")
    print("4. exit")

    while True:
        choice = input("\nEnter option: ").lower()

        if choice == "search book":
            name = input("Enter book name: ")
            search_book(name)

        elif choice == "filter price":
            price = float(input("Enter max price: "))
            filter_price(price)

        elif choice == "available books":
            filter_availability()

        elif choice == "exit":
            print("Goodbye 👋")
            break

        else:
            print("Invalid option")

chatbot()