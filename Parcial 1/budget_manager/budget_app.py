import budget_db as db

def main():
    while True:
        print("\n1. Add Article\n2. View Article\n3. Update Article\n4. Delete Article\n5. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            name = input("Enter name: ")
            description = input("Enter description: ")
            price = float(input("Enter price: "))
            db.add_article(name, description, price)
        elif choice == '2':
            article_id = int(input("Enter article ID: "))
            article = db.get_article(article_id)
            if article:
                print(f"Name: {article.name}, Description: {article.description}, Price: {article.price}")
            else:
                print("Article not found.")
        elif choice == '3':
            article_id = int(input("Enter article ID: "))
            name = input("Enter new name (leave blank to skip): ")
            description = input("Enter new description (leave blank to skip): ")
            price = input("Enter new price (leave blank to skip): ")
            price = float(price) if price else None
            if db.update_article(article_id, name, description, price):
                print("Article updated successfully.")
            else:
                print("Article not found.")
        elif choice == '4':
            article_id = int(input("Enter article ID: "))
            if db.delete_article(article_id):
                print("Article deleted successfully.")
            else:
                print("Article not found.")
        elif choice == '5':
            break
        else:
            print("Invalid choice, please choose again.")

if __name__ == '__main__':
    main()
